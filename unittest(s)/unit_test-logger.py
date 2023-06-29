class logger:


    def __init__(self,_log_file,_global_severity=0 ,_logobj= str):
        self._logobj=_logobj
        self._global_severity=_global_severity
        self._log_file=_log_file
    

    def info(self,_function_name,_message):
        import time
        log_file=open(self._log_file,"a+")
        log_file.write(time.ctime()+"at"+time.perf_counter_ns()+"    "+_function_name+"   called (local_severity=INFO)with message:  "+_message)
        log_file.close()


    def warning(self,_function_name,_message):
        import time
        log_file=open(self._log_file,"a+")
        log_file.write(time.ctime()+"at"+time.perf_counter_ns()+"    "+_function_name+"   called (local_severity=WARNING)with message:  "+_message)
        log_file.close()

    def critical(self,_function_name,_message):
        import time
        log_file=open(self._log_file,"a+")
        log_file.write(time.ctime()+"at"+time.perf_counter_ns()+"    "+_function_name+"   called (local_severity=CRITICAL)with message:  "+_message)
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


