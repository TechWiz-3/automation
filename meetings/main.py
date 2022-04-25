import datetime
from dotenv import load_dotenv
from os import getenv
from rich.console import Console
from webbrowser import open_new as open

pretty = Console()

load_dotenv()
MON_MORN = getenv("MON_MORN")
MON_AFT = getenv("MON_MORN")
TUES_MORN = getenv("MON_MORN")
TUES_AFT = getenv("MON_MORN")
THUR_ALLD = getenv("MON_MORN")

def what_day():
    """Returns the weekday"""
    if datetime.datetime.today().weekday() == 0:
        return "mon"
    elif datetime.datetime.today().weekday() == 1:
        return "tue"
    elif datetime.datetime.today().weekday() == 2:
        return "wed"
    elif datetime.datetime.today().weekday() == 3:
        return "thur"
    elif datetime.datetime.today().weekday() == 4:
        return "fri"
    elif datetime.datetime.today().weekday() == 5:
        return "sat"
    return "sun"

def what_time():
    current_date = datetime.datetime.now()
    return (current_date.time() < datetime.time(12))

def get_link():
    day = what_day()
    after_midday = what_time()
    if day == "mon":
        if after_midday:
            return MON_AFT
        return MON_MORN
    elif day == "tue":
        if after_midday:
            return TUES_AFT
        return TUES_MORN
    elif day == "wed":
        return False
    elif day == "thur":
        return THUR_ALLD
    elif day == "fri":
        return False
    elif day == "sat":
        return False
    return False

def main():
    link = get_link()
    if link == False:
        pretty.print("helloooooo", style = "green")
    else:
        pretty.print("You have a class now, that's so pog :sweat_smile: :sob:", style = "bold red")
        pretty.print(link, style = "blue underline")
        open(link)

main()