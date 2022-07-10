#!/bin/bash

export $(cat .env | xargs)  # load dotenv

gold_light="\033[38;5;136m"
gold_dark="\033[38;5;178m"
bold="\033[1m"
reset="\033[0m"

current_date=$(date '+%Y%m%d')  # get the date in integer form for the request
date_req=$(($current_date-1))  # get one day before

# api request
curl -skX GET "https://www.goldapi.io/api/XAU/AUD/$date_req" -H \
"x-access-token: $G_API_KEY" > gold_prices.json
price=$(jq '.price' gold_prices.json)

echo -e "
${bold}${gold_dark}Gold prices:${reset} AUD ${price}/oz
${gold_light}
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
${reset}
"
