#!/bin/bash

export $(cat .env | xargs)  # import env

curl -X POST -u "apikey:$API_KEY" \
--header "Content-Type: application/json" \
--header "Accept: audio/wav" --data "{\"text\":\"hello world and how are you today? i would like to talk about many things but first i would like to welcome the king Zac the Wise\"}" \
--output ~/Desktop/$RANDOM.wav "$LINK/v1/synthesize?voice=en-US_MichaelV3Voice"