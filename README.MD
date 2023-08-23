# Google Cloud Logging API

## Description

This is a simple python project that runs a series of methods to test log insertion into Google Cloud Logging API.

No setup file yet, just install whatever python tells you to install that you are missing.

## Setup

1. Create a Google Cloud Platform project.
2. Enable the Cloud Logging API and set up log storage.
3. Create a service account.
4. Download a service account key as JSON.
5. Place the JSON file into `config/` directory as `service_account.json`.

## Usage

To run the project, simply run the following command:

```bash
python test_logging.py
python3 test_logging.py
```

## Code

There are 2 Classes that help with the connection to the Google Cloud Logging API:

- `classes.GoogleAPI`:
  - This class is used to create a connection to the Google Cloud Logging API and handles credentials.
  - `Methods`:
    - `get_credentials()`:
      - This method is used to get the credentials from the `config/service_account.json` file.
    - `get_service_account_path()`:
      - This method is used to get the path to the `config/service_account.json` file.
- `classes.GoogleLogging`:
  This class is used to create a log entry and insert it into the Google Cloud Logging API.
  - `Methods`:
    - `log(logtext, severity)`:
      - This method is used to create a log entry and insert it into the Google Cloud Logging API.

3 Test Files:

- `example_error_1.py`
  - This file is used to test the logging of an error.
- `example_script_1.py`
  - This file is used to test the logging of an individual script.
- `example_script_2.py`
  - This file is used to test the logging of an individual script.

1 Main Test File:

- `test_logging.py`
  - This file is used to test the logging of all 3 test files.
