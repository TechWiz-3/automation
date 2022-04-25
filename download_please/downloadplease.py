from sys import platform as get_os
from os import system as cmd
from rich.console import Console
import yagmail
from os import getenv
from dotenv import load_dotenv

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
    yag.send(RECIPIENT, subject, contents)


def linux():
    pass

if __name__ == "__main__":
    # if get_os == 'darwin':
    #     mac_os()
    # elif 'linux' in get_os:
    #     linux()
    mac_os()