#Use Youtube API to do analysis on data provided by GOOGLE via Youtube.

#first you need to navigate to console.developers.google.com and sign in to get API Key.

#Create Project

#Enable API

#Use Youtube Data API

#Now create API key by clicking Create Credentials

#Answer questions

#Access Public Data

#What credentials do I need

#Now Google gives you API Key.

#NOW THE PROGRAM,

api_key = 'Ajdncs2-321ka193ijdancwfq'  #example API Key.

#one way to keep this safe is to use it as an environment variable for safekeeping.

#find documentations for Youtube API.

#Or GitHUb Youtube API Page for Python.

#now use, pip install google-api-python-client preferably in a Virtual Environment.

#open docs folder from Github

#NOW,

from googleapiclient.discovery import build

api_name = 'youtube'
api_version = 'v3'
youtube_service = build(api_name, api_version, developerKey = api_key)

#now use Instance methods provided in documentation to use the API.

#goto Youtube documentation and click on References. and Goto Channels Reference.

#scroll down to paramters and find arguments you can pass to the service.

#such as,

request = youtube_service.channels().list(
    part='statistics',
    forUsername='schafer5' #username different than display name.
)

response = request.execute()

print(response)

#For example we can use this API to create a service that Calculates the duration of videos in a specific playlist.
