# Imports the Cloud Logging client library
from google.auth import load_credentials_from_file
from dotenv import load_dotenv
import os


class GoogleAPI:
    '''
    Load Google API credentials from config/config.env file and create a Google Cloud API client object
    '''
    
    def __init__(self):
        try:
            load_dotenv('config/config.env')
            self.set_credentials(os.getenv('GOOGLE_SERVICE_ACCOUNT_PATH'))
        except Exception as err:
            print(err)
            raise err
        
    def set_credentials(self, json_path):
        '''
        Set the credentials for the Google API client object
        
        Parameters
        ----------
        json_path : str
            The path to the Google API credentials file
            
        Returns
        -------
        bool
            True if the credentials were set successfully, otherwise False
            
        Raises
        ------
        ValueError
            If json_path is None, is not a .json file, or is not a file
        FileNotFoundError
            If json_path does not exist
        '''
        if not json_path:
            raise ValueError('json_path cannot be None')
        elif not os.path.exists(json_path):
            raise FileNotFoundError(f'File not found: {json_path}')
        elif not json_path.endswith('.json'):
            raise ValueError('json_path must be a .json file')
        elif not os.path.isfile(json_path):
            raise ValueError(f'json_path must be a file, not a directory: {json_path}')
        else:
            self.json_path   = json_path
            self.credentials = load_credentials_from_file(self.json_path)
            return True
         
    def get_credentials(self):
        return self.credentials
    
    def get_service_account_path(self):
        return self.json_path
