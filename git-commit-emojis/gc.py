#!/usr/bin/env python3

# Zac the Wise on 24 May
# Little script that adds emojis and labels for git commits
# More info: https://github.com/TechWiz-3/automation/tree/main/git-commit-emojis

from sys import argv  # import cli arguement function
from sys import exit  # import exit function
from os import system

def help():
    """Help command"""
    print(
        "\n\n"\
        "Git emoji/labeling tool created by Zac the Wise"\
        "\n\n"\
        "Usage:",
        "\n\n"\
        "gc -m <commit message>"\
        "\n\n"\
        "      -h, --help      shows this command"\
        "\n\n"\
        "      -m <\"message\">     commit message (required), use quotation marks"\
        "\n\n"
    )

def get_opts():
    """Get cli options/arguements"""
    for arg in argv[1:]:  # gets arguements except the first one and assigns them
        if arg == "-m":  # message option
            # get the argument for the option
            get_arg_index = argv.index('-m')  # find the index number for the option
            commit_message = argv[get_arg_index+1]  # get the arguement after the option and assign it
            return commit_message
        elif arg == "-h" or arg == "--help":  # help option
            help()  # display help message
            return exit()  # stop the rest of the program from running

def select_menu():
    """Displays the select menu and returns the value to enter into the commit"""
    options = ["👌 Improvement", "📦 Addition", "📖 Documentation", "🐛 Bug-fix", "🔖 Version-tag", "🚪 Exit"]
    commit_label = ""
    for option in options:
        opt_no = options.index(option)
        print(f"{opt_no+1}) {option}")
    select_label = int(input("Enter the number corresponding to which type of change you made: "))
    if select_label == 1:
        commit_label = "👌 IMPROVE: "
    elif select_label == 2:
        commit_label="📦 NEW: "
    elif select_label == 3:
        commit_label="📖 DOC: "
    elif select_label == 4:
        commit_label="🐛 FIX: "
    elif select_label == 5:
        commit_label="🔖 "
    elif select_label == 6:
        print("Exiting, have a nice day...")
        exit()
    return commit_label

commit_msg = get_opts()
label = select_menu()

system(f"git commit -m \"{label}{commit_msg}\"")

