# Created by Zac the Wise
# A tool that can play music from a local folder in a playlist sort of way
# no more spotify or itunes
# In the future I will add tools that will allow the construction of said
# playlists using yt and spotify download tools

import glob
from playsound import playsound

# default playlist folder for the time being
playlist_folder = '/Users/Peregrine/Desktop/Other Music/'
folder_items = glob.glob(f"{playlist_folder}*.mp*")  # get mp3 and mp4
for item in folder_items:
    print(f"Now playing, {item}")
    playsound(item)