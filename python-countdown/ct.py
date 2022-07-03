# Create by Zac the Wise
# Python countdown script with a ringing noise

from time import sleep
from playsound import playsound

type = int(input("Type:\n\n1: seconds\n2: minutes\n3: hours\n"))
how_long = int(input("How long? "))
if type == 1:
    timer(how_long)
elif type == 2:
    timer(how_long*60)
elif type == 3:
    timer(how_long*60*60)

def timer(seconds: int) -> None:
    sleep(how_long)
    print("Times up")
    playsound(
        '/Users/Peregrine/Desktop/Projects/Automation/python-countdown/ringer.mp3'
    )
