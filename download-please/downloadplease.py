# Script to automate sending
# emails requesting videos to
# be downloaded
# Created by Zac the Wise on 25/April/2022

from sys import platform as get_os
from os import system as cmd
from rich.console import Console
import yagmail
from os import getenv
from dotenv import load_dotenv
from plyer import notification

pretty = Console()
yag = yagmail.SMTP('programmingplus1@gmail.com')

load_dotenv()
RECIPIENT = getenv("RECIPIENT")

contents = ["Please download the following when you get the time, thank you :)"]
subject = "Please Download "

def mac_os():
    pretty.print("Welcome to Download Please", style = "Green Yellow Underline")
    #cmd("say Welcome to download please")
    link = pretty.input("[purple]Enter link here [/purple]")
    contents.append(link)
    while link != "x":
        pretty.print("Enter another link or x to escape", style = "Green")
        link = pretty.input("[purple]Enter link here [/purple]")
        if link == "x":
            break
        else:
            contents.append(link)
    add_subject = pretty.input("[green]Enter subject[/green] ")
    global subject
    subject += add_subject
    try:
        yag.send(RECIPIENT, subject, contents)
    except:
        print("Error occured sending email")
        notification.notify(title='Error occured', message='Error occured sending email', app_name='Download Please App', app_icon='', timeout=10, ticker='', toast=False)
    else:
        notification.notify(title='Email Sent Successfully', message='Email sent successfully', app_name='Download Please App', app_icon='', timeout=10, ticker='', toast=False)

def linux():
    pass

if __name__ == "__main__":
    # if get_os == 'darwin':
    #     mac_os()
    # elif 'linux' in get_os:
    #     linux()
    mac_os()