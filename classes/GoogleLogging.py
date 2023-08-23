import os
import inspect
import google.cloud.logging_v2 as GoogleLoggingAPI
from classes.GoogleAPI import GoogleAPI


class GoogleLogging(GoogleAPI):
    '''
    Create a Google Cloud Logging logger object

    Parameters
    ----------
    log_name : str, optional
        The name of the log to write to. The default is None.
        If None, the name of the script that called this function will be used.
    '''

    def __init__(self, log_name=None):
        
        super().__init__()                          # Call the __init__ function of the parent class
        src = inspect.stack()[1][1].split('\\')[-1] # Get the name of the script that called this function
        
        self.source      = src if src.endswith('.py') else ''                    # If the script name ends with .py, use it. Otherwise, use ''
        self.credentials = GoogleAPI().get_credentials()[0]                      # Get the credentials from the GoogleAPI class
        self.client      = GoogleLoggingAPI.Client(credentials=self.credentials) # Create a Google Cloud Logging client object
        self.logname     = log_name if log_name else self.source                 # If a log name was provided, use it. Otherwise, use the script name
        self.logger      = self.client.logger(self.logname)                      # Create a Google Cloud Logging logger object

    def log(self, text, severity='DEBUG'):
        '''
        Log a message to Google Cloud Logging

        Parameters
        ----------
        text : str
            The text to log
        severity : str, optional
            The severity of the log message. The default is "DEBUG".
            
            Must be one of the following: [DEBUG, INFO, NOTICE, WARNING, ERROR, CRITICAL, ALERT, EMERGENCY] 
        '''
        
        valid_severities = ['DEBUG', 'INFO', 'NOTICE', 'WARNING', 'ERROR', 'CRITICAL', 'ALERT', 'EMERGENCY']
        
        if severity not in valid_severities:
            self.log(f'Invalid severity: {severity}', severity='CRITICAL')
        else:
            log_text = f'[{severity}] :: [{self.source}] :: [{text}]'
            self.logger.log_text(log_text, severity=severity)
