# Simple automated script that provides me
# with the MS Teams link for my classes
# based on the date and time
# Created by Zac the Wise on 25/April/2022

import datetime
from dotenv import load_dotenv
from os import getenv
from rich.console import Console
from webbrowser import open_new as open
from subprocess import call as open_folder

pretty = Console()

load_dotenv()
MON_MORN = getenv("MON_MORN")
MON_AFT = getenv("MON_AFT")
TUES_MORN = getenv("TUES_MORN")
TUES_AFT = getenv("TUES_AFT")
THUR_ALLD = getenv("THUR_ALLD")

MON_MORN_F = getenv("MON_MORN_F")
MON_AFT_F = getenv("MON_AFT_F")
TUES_MORN_F = getenv("TUES_MORN_F")
TUES_AFT_F = getenv("TUES_AFT_F")
THUR_ALLD_F = getenv("THUR_ALLD_F")

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
    """Returns if the current time is after midday or not"""
    current_date = datetime.datetime.now()
    return (current_date.time() > datetime.time(12))

def get_link():
    day = what_day()
    after_midday = what_time()
    print(after_midday)
    if day == "mon":
        if after_midday:
            return MON_AFT, MON_AFT_F
        return MON_MORN, MON_MORN_F
    if day == "tue":
        if after_midday:
            return TUES_AFT, TUES_AFT_F
        return TUES_MORN, TUES_MORN_F
    elif day == "wed":
        return False, False
    elif day == "thur":
        return THUR_ALLD, THUR_ALLD_F
    elif day == "fri":
        return False, False
    elif day == "sat":
        return False, False
    return False, False

def main():
    link, folder = get_link()
    if link == False:
        pretty.print("No classes today, now that's actually pog", style = "green")
    else:
        pretty.print("You have a class now, that's so pog :sweat_smile: :sob:", style = "bold red")
        pretty.print(link, style = "blue underline")
        open(link)  # type: ignore
        open_folder(["open", "-R", folder])  # type: ignore


main()