#!/usr/bin/env python3

from datetime import datetime
import json
import requests
from os import getenv
from dotenv import load_dotenv

regular_print = False
pretty = None
try:
    from rich.console import Console
except ImportError:
    regular_print = True
else:
    pretty = Console()

load_dotenv()
API_KEY = getenv("G_API_KEY")

gold = """
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣟⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠀⠈⠙⢿⣿⣿⣿⣿⠟⢁⣠⣀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠈⠻⣿⣧⡾⠟⠉⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⣀⣤⡶⠟⠋⠁⠀⠀⠀⠀⣀⣄⡉⠛⠿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡿⠞⠋⠁⠀⠀⠀⠀⣀⣤⣶⠿⠛⢉⣠⡴⠾⠛⣿⣤⣿⣿
⣿⣛⠋⢩⣷⠟⠋⢁⣤⣄⡀⠀⣀⣤⣶⠿⠛⠉⣠⣴⠾⠛⠁⠀⠀⠀⠸⣿⣿⣿
⣿⣿⣿⣾⠛⠷⣦⣄⡈⠙⠿⡿⠟⠋⣀⣤⡶⠟⠋⠀⠀⠀⠀⠀⠀⢀⣤⣿⣿⣿
⣿⣿⣿⠇⠀⠀⠀⠉⠛⠷⣦⣤⡶⠟⠋⠁⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⣿⣿
⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⢸⡏⠀⠀⠀⠀⠀⢀⣠⣴⠾⠛⠉⠀⠙⢿⣿⣿⣿⣿
⣿⣿⣿⣿⣷⣦⣄⡀⠀⠀⢸⡇⠀⢀⣠⣴⠾⠛⠉⣤⣤⣀⣀⡀⠀⠈⢻⣿⣿⣿
⣿⣿⣿⣿⣿⡿⠉⠻⢷⣤⣼⣧⣶⣟⠋⠁⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿
⣿⣿⣿⣿⣿⣧⣶⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
"""

today = datetime.today().strftime("%Y%m%d")  # get current date for request
today = int(today) - 1  # convert to integer and get previous day

request_url = f"https://www.goldapi.io/api/XAU/AUD/{today}"
headers = {'x-access-token': API_KEY}

request_response = requests.get(request_url, headers=headers)
gold_data = json.loads(request_response.content)
try:
    gold_price = gold_data["price"]
except KeyError:
    print("An error occured and the request for gold price returned an error message.")
    gold_price = "Gold price not found"

if regular_print:
    print(gold_price)
else:
    pretty.print(f"\n[#FFD700]Gold price: AUD {gold_price}/oz\n{gold}[/#FFD700]\n") # type: ignore

