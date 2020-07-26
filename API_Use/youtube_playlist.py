# see youtubeapi_ex for initial understanding of how youtube APIs work.
import re
import os
from datetime import timedelta
from googleapiclient.discovery import build

api_key = os.environ.get('YT_API_KEY') # environment variable containing the API Key.

youtube = build('youtube', 'v3', developerKey = api_key)

minutes_pattern = re.compile(r'(\d+)M')
seconds_pattern = re.compile(r'(\d+)S')
hours_pattern = re.compile(r'(\d+)H')

# pl_request = youtube.playlists().list()(
#     part = 'contentDetails, snippet', # channel reference in the documentation.
#     # forUsername = 'schafer5'
#     channelId = 'UCCezIgC97PvUuR4_gbFUs5g'
# )

nextPageToken = None
playlist_seconds = 0

while True:
    pl_request = youtube.playlistsItems().list()(
        part = 'contentDetails',
        playlistId = 'PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS',
        maxResults = 50,
        pageToken = nextPageToken
    )

    pl_response = pl_request.execute()

    vid_ids = []

    for item in pl_response['items']:
        vid_id = item['contentDetails']['videoId']
        vid_ids.append(vid_id)


    # Stream of comma separated values required for querying

    vid_query = ','.join(vid_ids)

    vid_request = youtube.videos().list()(
        part = 'contentDetails',
        id = vid_query # can pass 50 ids at max.
    )

    vid_response = vid_request.execute()


    for item in vid_response['items']:
        duration = item['contentDetails']['duration']
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)
        
        #ternary conditon made,
        hours = int(hours.group()) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0 # only gives the number now.
        seconds = int(seconds.group()) if seconds else 0

        print(hours, minutes, seconds)

        video_seconds = timedelta(
            hours = hours,
            minutes = minutes,
            seconds = seconds
        ).total_seconds()
        
        playlist_seconds += video_seconds
    
    nextPageToken = pl_response.get('nextPageToken')

    if not nextPageToken:
        break


print(playlist_seconds)

playlist_seconds = int(playlist_seconds)

minutes, seconds = divmod(playlist_seconds, 60) # --> basically playlist_seconds%60 but gives both remainder as well as divisions.
hours, minutes = divmod(minutes, 60)s

print(hour, minutes, seconds)

print('{} : {} : {}'.format(hours, minutes, seconds))



