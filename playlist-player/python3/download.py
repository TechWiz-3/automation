from pytube import YouTube
from rich.console import Console
from playsound import playsound
from os import chdir
from os.path import expanduser

pretty = Console()
location = ''

type = pretty.input("[purple]Download is classical (a) or other (b)? [/purple]")
video_input = pretty.input("[green]Enter youtube video (x to escape) [/green]")
while video_input.lower() != "x":
    if type.lower() == "a":
        location= '~/Desktop/Classical'
    elif type.lower() == "b":
        location= '~/Desktop/Non classical'
    chdir(expanduser(location))
    yt_vid = YouTube(video_input)
    try:
        yt_vid.streams.filter(type="audio").first().download()
    except Exception as error:
        print("Error occured")
    else:
        pretty.print("[#3de048]Download successful :))[/#3de048]")
    
    video_input = pretty.input("[green]Enter youtube video (x to escape) [/green]")
