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

today = datetime.today().strftime("%Y%m%d")  # get current date for request
today = int(today) - 1  # convert to integer and get previous day

request_url = f"https://www.goldapi.io/api/XAU/AUD/{today}"
headers = {'x-access-token': API_KEY}

request_response = requests.get(request_url, headers=headers)
gold_data = json.loads(request_response.content)
gold_price = gold_data["price"]

if regular_print:
    print(gold_price)
else:
    pretty.print(f"[#FFD700]Gold price: AUD {gold_price}/oz[/#FFD700]")



