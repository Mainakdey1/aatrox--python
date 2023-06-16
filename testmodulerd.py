import logging
import psutil
import messages
import datetime
from telegram import __version__ as TG_VER
from telegram import Bot
from messages import TelegramBot
import os


__version__=0.12

tolken="6199318379:AAGmrDxxhYeYWabD8MqyrMMwKvVztDkPhGE"










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
botinst=Bot(tolken)

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
    os.system('shutdown -s')

def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(tolken).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("shutdown",shutdown))

    # on non command i.e message - echo the message on Telegram
    
    application.add_handler(CommandHandler("getupdate",getupdate))
    # Run the bot until the user presses Ctrl-C
    application.run_polling()
    

btime=datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
messageobj=TelegramBot(auth=tolken,chat_id='820919205',body='The service was started at'+' '+btime)
messageobj.send()

if __name__ == "__main__":

    main()

