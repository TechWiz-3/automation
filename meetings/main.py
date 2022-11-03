# Simple automated script that provides me
# with the MS Teams link for my classes
# based on the date and time
# Created by Zac the Wise on 25/April/2022

import datetime
from dotenv import load_dotenv
from os import getenv
from rich.console import Console
import webbrowser
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


def what_day() -> str:
    """Returns the weekday"""
    full_date = datetime.datetime.now()
    # format time to the weekday as locale’s abbreviated name
    formatted_date = full_date.strftime("%a")
    return str(formatted_date)


def what_time():
    """Returns if the current time is after midday or not"""
    current_date = datetime.datetime.now()
    return (current_date.time() > datetime.time(12))


def get_link() -> tuple:
    day = what_day()
    after_midday = what_time()
    if day == "Mon":
        if after_midday:
            return MON_AFT, MON_AFT_F
        return MON_MORN, MON_MORN_F
    if day == "Tue":
        if after_midday:
            return TUES_AFT, TUES_AFT_F
        return TUES_MORN, TUES_MORN_F
    elif day == "Wed":
        return False, False
    elif day == "Thur":
        return THUR_ALLD, THUR_ALLD_F
    elif day == "Fri":
        return False, False
    elif day == "Sat":
        return False, False
    return False, False


def main():
    link, folder = get_link()
    if not link:
        pretty.print("No classes today, now that's actually pog", style="green")
        print("")
    else:
        pretty.print(
            "You have a class now, that's so pog :sweat_smile: :sob:", style="bold red"
        )
        pretty.print(link, style="blue underline")
        webbrowser.open_new(link)
        open_folder(["open", "-R", folder])  # type: ignore


main()
