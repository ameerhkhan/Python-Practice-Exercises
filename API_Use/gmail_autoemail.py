# Original Article --> How to automate your email with Python by SeattleDataGuy.
# Link --> https://medium.com/better-programming/how-to-automate-your-emails-with-python-386b4e2d5395

# Two steps to this program,
# 1 - Pull data from a URL whenever there is a new dataset
# 2 - Send an email using Google's GMAIL API.

# Pre-requisites:
# 1) Create a project at the Google API console at the top-left of GDC
# 2) Enable Gmail API by clicking 'Library' on the left sidebar
# 3) Create OAuth client ID credentials at the top sidebar
# 4) Quickstart guide for Python in URL (see below)
# 5) pip install --upgrade google-api-python-client \
# google-auth-httplib2 google-auth-oauthlib
# 6) Access to Gmail
# 7) Create the e-mail

# Download a text file with the last updated date or even data,
# If the file is different send an email.

# Google API imports
from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


import requests

# To run a loop based on time intervals.
import time

from datetime import datetime, timedelta
import math

# To create emails,
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import base64
import os

# if modifying these scopes, delete the file token.pickle??
# You need this scope for full access to Google mail API.

SCOPES = 'https://mail.google.com/'

# Following function will help in sending the email with the Gmail API.

def create_message(sender, to, subject, csv):
    message = MIMEMultipart()
    message['from'] = sender
    message['to'] = to
    message['subject'] = subject


    # write the Time it was last updated in the body of the email.
    dt_obj = datetime.utcnow() - timedelta(hours=7)
    msg = MIMEText('Hello, Your file was updated.' \
        '\n Time of update: ' + dt_obj.strftime('%m/%d/%Y, %I : %M : %S %p') \
            + '(Los Angeles Time)')
    
    message.attach(msg)

    # Attach the csv file
    record = MIMEBase('application', 'octet-stream')

    record.set_payload(csv)
    encoders.encode_base64(record)
    record.add_header('Content-Disposition', 'attachment', filename='medicare.csv')
    message.attach(record)


    # Return the message
    raw = base64.urlsafe_b64encode(message.as_bytes()) # This will set the message in bytes to easily transfer the data to GMAIL API.
    raw = raw.decode()
    
    return {'raw': raw}


# Now a function to send the message
def send_message(service, user_Id, message):
    try:
        message = service.users().messages() \
                                .send(userId=user_Id, body=message) \
                                .execute()
        print('Message Id: %s' % message['id'])
        return(message)
    except Exception as e:
        print('An error occurred %s' % e)
        return None

# 1 - Fetch the DATA.
# Get the webpage store it in a response object and assign the text.

# This URL contains the .csv download of
# 'https://catalog.data.gov/dataset/' \
#	'share-of-medicaid-enrollees-in-managed-care'
# used to send to the destination e-mail.
csvFileURL = 'https://data.medicaid.gov/api/views/u72p-j37s/rows.csv?accessType=DOWNLOAD'

csv_request = requests.get(csvFileURL)
csv_file = csv_request.content

# COMMENTED OUT: The below is necessary if file is not .csv.
# Now we add the important SEP metadata command.
# This tells Excel to use a delimiter.
#decoded = csvFile.decode('utf-8')
#decoded = 'SEP=,\n' + decoded
#csvFile = decoded.encode('utf-8')

# This URL contains the .json download of
# 'https://catalog.data.gov/dataset/' \
#	'share-of-medicaid-enrollees-in-managed-care'
# used to compare files.
json_file = 'https://data.medicaid.gov/api/views/u72p-j37s/rows.json?accessType=DOWNLOAD'

r = requests.get(json_file)
first_json = r.text



# 2 - Use the Google API to send an email with the updated METADATA.

# Find out whether the file was changed or not.

# The code compares .json file version every minute to track any changes.
# This will run the code every 60 seconds.

r = requests.get(json_file)
second_json = r.text

# if the site was updated or the script just began,

if first_json != second_json:

    # Create the message
    sender = 'sender@gmail.com'
    to = 'email_id@someemail.com'
    subject = 'The Medicare METADATA has been updated'
    message = create_message(sender, to, subject, csv_file)

    # send the message using the Google API
    creds = None
    
    # The file token.pickle stores the users ACCESS and REFRESH tokens, and is,
    # created automatically when the authorization flow completes for the first time.

    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # If there are no valid credentials available let the user log in.

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

        else:

            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)


    service = build('gmail', 'v1', credentials=creds)
    send_message(service, sender, message)

    # Update the variable

    first_json = second_json

    print('Message SENT!!')
 



