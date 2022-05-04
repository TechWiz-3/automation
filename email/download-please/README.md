# Download Please

## What
Automated script that allows the user to send an email through a terminal to a specified recipient asking for user inputted video links to be download.

## Who
Created by Zac the Wise  
Inspired by the amount of times I have sent such emails

## How
Using python3 with the following libraries used
- yagmail (for managing email client)
- keyring (for managing email client credentials)
- rich (for enriching terminal output)
- python-dotenv (for accessing environment variables)
- plyer (for notifictions)

## Logic
Uses a main function with try excepts to catch if an error occurs while attempting to send the email.
