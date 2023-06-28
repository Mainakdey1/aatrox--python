# Python Spyware

## This is a self updating Python script that utilizes Telegram's python-telegram-bot to spy on a single system. The script allows the following features in a single script:

Thing about a python spyware is that, since python is not a part of the packages that come with Windows as part of it's build, a spyware made with python makes not a lot of sense compared to it's C/C++ counter parts. But what's in trying anyway?



- Automatic dependency management: This will allow the script to download it's packages using pip without any prompt to the host system.
- A single script self updating system: Upon startup, the script runs and checks for updates on it's Github page for updates. If it finds one, it updates itself.
- System rights elevation(under work): The script can access the terminal under Administrative rights, by performing a UAC elevation, under Python organization's name which gives it access to the entire system.
- A custom logging class, for program specific logging(also I could'nt make sense of python's loggingmodule. yes im dumdum) and a log file retriever method, for remote maintenance.



## Methods supported currently by the program(for system control):
- Access to all OS level information and procceses(currently) running in the host system.
- Screen Capture: Returns a screenshot to the user of the host system's monitor.
- Pop up messages(Strictly for scaring people)
- remote user file access(using terminal under Elevated Administrative Rights)
- Remote shutdown



## How to use this program in your own machine:
"""
This program requires python 3.11 and above to run. It also makes use of pip to install it's packages; if pip is not installed, it will throw an exception.

Download this script in your system and (ideally) place it in your Python folder and you're done!
Not really.

You need to change the token present in the file to your own telegram token. This is actually pretty easy.
Make a telegram account and then search for Bot Father. Follow the steps and make your own bot. Use it's methods to obtain the token for your bot.
That's it(really it). You can now use this bot to send commands to your computer or someone else's computer(evil laugh).

You will require some intuition to make the script run but I believe in you.

Small story: I really made this program to prank my unsuspecting friends in my college department. I kept adding features thinking of various ways to do so
and in the end it became this instead.

Made with a healthy amount of hate towards my school.

### Please do not use this program for malicious purposes. However clever you think you are, there's always a cop that's smarter. 
### With crime thy shall not get away, for Jail is never too far away.
