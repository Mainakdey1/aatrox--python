# Python Spyware

This is a self updating Python script that utilizes Telegram's python-telegram-bot to spy on a single system. The script allows the following features in a single script:


1.Automatic dependency management: This will allow the script to download it's packages using pip without any prompt to the host system.
2.A single script self updating system: Upon startup, the script runs and checks for updates on it's Github page for updates. If it finds one, it updates itself.\n
3.System rights elevation(under work): The script can access the terminal under Administrative rights, by performing a UAC elevation, under Python organization's name which gives it access to the entire system.
4. A custom logging class, for program specific logging(also I could'nt make sense of python's loggingmodule. yes im dumdum) and a log file retriever method, for remote maintenance.



Methods supported currently by the program(for system control):
i. Access to all OS level information and procceses(currently) running in the host system.
ii. Screen Capture: Returns a screenshot to the user of the host system's monitor.
iii. Pop up messages(Strictly for scaring people)
iv.Remote user file access(using terminal under Elevated Administrative Rights)
v.Remote shutdown



How to use this program in your own machine:

This program requires python 3.11 and above to run. It also makes use of pip to install it's packages; if pip is not installed, it will throw an exception.

Download this script in your system and (ideally) place it in your Python folder and you're done!
Not really.

You need to change the token present in the file to your own telegram token. This is actually pretty easy.
Make a telegram account and then search for Bot Father. Follow the steps and make your own bot. Use it's methods to obtain the token for your bot.
That's it(really it). You can now use this bot to send commands to your computer or someone else's computer(evil laugh).

You will require some intuition to make the script run but I believe in you.

Small story: I really made this program to prank my unsuspecting friends in my college department. I kept adding features thinking of various ways to do so
and in the

