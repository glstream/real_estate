from twython import Twython
from auth import *
import os
from OS_NAME_PATHS import *

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
formatted_message = '#Seattle #seattlerealestate #realestate'
all_files = []
for root, dirs, files in os.walk(viz_dir):
    for file in files:
        if 'condo' not in file:
            all_files.append(os.path.join(root, file))
            print(file)
            
for full_file in all_files:
    image = open(full_file, 'rb')
    response = twitter.upload_media(media=image)

    twitter.update_status(status=formatted_message, media_ids=[response['media_id']])
    print("Tweeted: %s" % formatted_message)