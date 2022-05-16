#!/bin/bash
# This script does not work for me, it returns corrupted audio files (without errors) that
# ONLY vlc media player can intepret


export $(cat .env | xargs)  # import env

rand_name="$RANDOM"

curl -X POST -u "apikey:$API_KEY" \
--header "Content-Type: application/json" \
--header "Accept: audio/wav" \
--data "{\"text\":\"Hello world\"}" --output hello.wav "$LINK/v1/synthesize?voice=en-US_MichaelV3Voice"

afplay please_work.mp3