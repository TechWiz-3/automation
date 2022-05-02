#!/bin/bash

export $(cat .env | xargs)  # load dotenv

current_date=$(date '+%Y%m%d')  # get the date in integer form for the request
date_req=$(($current_date-1))  # get one day before

# api request
curl -skX GET "https://www.goldapi.io/api/XAU/AUD/$date_req" -H \
"x-access-token: $G_API_KEY" > gold_prices.json
price=$(jq '.price' gold_prices.json)

echo -e "
Gold prices: AUD $price/oz

⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⡏⠻⣿⣿⣿⣿⠏⠀⢸⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡀⠙⢿⣿⣿⣿⡇⠀⠈⢿⣿⠋⠀⠀⠸⣿⣿⠟⢡⣿⣿⣿⠿⢫⣿⣿
⣿⣿⣿⣿⣧⠀⠀⠙⢿⣿⡇⠀⢀⣀⣁⣀⣀⡀⠀⠛⠁⢠⣿⠿⠋⠁⢀⣿⣿⣿
⣿⣿⠙⢿⣿⣇⠀⠀⠀⠉⠀⢠⡟⠉⠉⠉⠉⢻⡄⠀⠀⠋⠀⠀⠀⠀⣾⣿⣿⣿
⣿⣿⡆⠀⠈⠻⡄⠀⢀⣶⠶⠾⠷⢶⣶⣶⡶⠾⠷⠶⣶⡀⠀⠀⠀⣼⠟⠋⠁⣿
⣿⣿⣧⠀⠀⢀⣀⣀⣼⣇⣀⣀⣀⣀⣿⣿⣀⣀⣀⣀⣸⣧⣀⣀⡈⠀⠀⠀⠀⣿
⣿⠉⠋⠀⠀⣾⠋⠉⠉⠉⠙⣿⡟⠉⠉⠉⠉⢻⣿⠋⠉⠉⠉⠙⣷⠀⠀⠀⠀⣿
⣿⠀⣼⠟⠛⠛⠛⢿⣿⡿⠛⠛⠛⠻⣿⣿⠟⠛⠛⠛⢿⣿⡿⠛⠛⠛⠻⣧⠀⣿
⣿⣴⣿⣤⣤⣤⣤⣼⣿⣧⣤⣤⣤⣤⣿⣿⣤⣤⣤⣤⣼⣿⣧⣤⣤⣤⣤⣿⣦⣿
⣿⠀⠀⠀⣿⣿⡁⠀⠀⠀⢈⣿⣏⠀⠀⠀⠀⣹⣿⡁⠀⠀⠀⢈⣿⣿⠀⠀⠀⣿
⣿⣿⣿⠋⠉⠉⠉⢻⣿⡟⠉⠉⠉⠙⣿⣿⠋⠉⠉⠉⢻⣿⡟⠉⠉⠉⠙⣿⣿⣿
⣿⣿⣿⣶⣶⣶⣶⣾⣿⣷⣶⣶⣶⣶⣿⣿⣶⣶⣶⣶⣾⣿⣷⣶⣶⣶⣶⣿⣿⣿"