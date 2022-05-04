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

def main():
    """Main function"""
    contents = ["Check this out, I think you might like it ;)"]
    subject = "Check this out "
    link = pretty.input("[purple]Enter link[/purple] ")
    contents.append(link)
    while link.lower() != "x":
        link = pretty.input("[purple]Enter link[/purple] ")
        if link == "x":
            break
        contents.append(link)
    add_subject = pretty.input("[blue]Enter subject[/blue] ")
    subject += add_subject
    try:
        yag.send(RECIPIENT, subject, contents)
    except:
        print("Error occured sending email")
        notification.notify(
            title='Error occured',
            message='Error occured sending email',
            app_name='Check this out', app_icon='',
            timeout=10, ticker='',
            toast=False
                ) # type: ignore 
    else:
        pretty.print("[green]Email sent successfully[/green]")
        notification.notify(
            title='Email Sent Successfully',
            message='Email sent successfully',
            app_name='Check this out',
            app_icon='',
            timeout=10,
            ticker='',
            toast=False
                ) # type: ignore 

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pretty.print("[red]Exiting[/red]")