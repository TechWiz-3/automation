# Meetings
![Image](https://img.shields.io/badge/CROSS%20PLATFORM-YES-success?style=for-the-badge)

Things you'll need to change before use:
```
1. Line 8 of class - change the path to your own
2. Follow installation guide as specified in lines 3-7 of class
   (Please note if on windows, the class shell script likely won't work outside of git bash, however the python script should work fine)
3. Create a .env with the following variables
   MON_MORN, MON_AFT, TUES_MORN, TUES_AFT, THUR_ALLD - these contain the meeting links
   MON_MORN_F, MON_AFT_F, TUES_MORN_F, TUES_AFT_F, THUR_ALLD_F - these contain the paths to the class folders
4. Adjust the get_link function and the env variable names if necessary to fit your schedule
```

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
