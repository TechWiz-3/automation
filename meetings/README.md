# Meetings
![Image](https://img.shields.io/badge/CROSS%20PLATFORM-YES-critical&style=for-the-badge)
## What
Simple automated script that provides me with the MS Teams link for my classes based on the date and time.  
## Who
Created by Zac the Wise on 25/April/2022  
## How
Using Python 3.9 with the following libraries used
- Datetime to check the day and time
- [Python-dotenv](https://pypi.org/project/python-dotenv/) to store the meeting links
- OS module to load the ENV
- Webbrowser module to open the links
- [Rich python](https://github.com/Textualize/rich) to give the terminal output extra colour
## Logic
Three functions and a main function are used.  


**`what_day`** uses the datetime module to return the weekday  

**`what_time`** uses the datetime module to return true or false if the current time is after midday or not  

**`get_link`** uses the values from `what_day` and `what_time` to fetch the right links or return false if a class isn't on that day.  

**`main`** checks the results of `get_link` and then either prints to the terminal that no class is on, or prints the link to the terminal as well as opening it in the default web browser using the python webbrowser module.
