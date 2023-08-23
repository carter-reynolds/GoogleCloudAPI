from classes.GoogleLogging import GoogleLogging
import traceback

def run_error():
    
    try:
        x_string = "10a"
        x_int = int(x_string)
        print(x_int)
  
    except ValueError:
        GoogleLogging().log(traceback.format_exc(), severity='ERROR')
        GoogleLogging().log(traceback.format_exc(), severity='WARNING')
        GoogleLogging().log(traceback.format_exc(), severity='CRITICAL')
        GoogleLogging().log(traceback.format_exc(), severity='ALERT')
        GoogleLogging().log(traceback.format_exc(), severity='EMERGENCY')
     
