import logging
import sys
import subprocess
import pkg_resources

required={"python-telegram-bot","psutil","datetime","messages","win10toast"}
installed={pkg.key for pkg in pkg_resources.working_set}
missing=required-installed
if missing:
    subprocess.check_call([sys.executable,"-m","pip","install",*missing])




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






import telegram.ext as tg
import psutil
import datetime
from messages import TelegramBot
import os
from win10toast import ToastNotifier
import tkinter 
from tkinter import messagebox
import pyautogui


tolken="6199318379:AAGmrDxxhYeYWabD8MqyrMMwKvVztDkPhGE"



    
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)
# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")

async def getupdate(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    btime=psutil.boot_time()
    ftime=datetime.datetime.fromtimestamp(btime).strftime("%Y-%m-%d %H:%M:%S")
    processdict=[ftime,"\n\n"]
    for process in psutil.process_iter():
        processdict+=[process.name(),]
    await update.message.reply_text(processdict)
async def shutdown(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    os.system('shutdown -s -t 0')
async def cpu_time(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    await update.message.reply_text(psutil.cpu_percent())
async def show_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    _message=update.message.text
    _tkobj=tkinter.Tk().withdraw()
    messagebox.showinfo("Messenger from Alexandria",_message)
    #toaster=ToastNotifier()                  deprecated
    #toaster.show_toast("Windows",_message)  

async def image_grab(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    img_grab=pyautogui.screenshot()
    img_grab.save("image1.png")
    await update.message._bot.sendDocument(update.message.chat_id,open("image1.png","rb"))
    print("sent")


    
  

def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(tolken).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("shutdown",shutdown))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(CommandHandler("cpu",cpu_time))
    application.add_handler(CommandHandler("getupdate",getupdate))
    application.add_handler(CommandHandler("sc",image_grab))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, show_message))
    # Run the bot until the user presses Ctrl-C
    application.run_polling()
btime=datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
messageobj=TelegramBot(auth=tolken,chat_id='820919205',body='The service was started at'+' '+btime)
messageobj.send()

if __name__ == "__main__":

    main()

