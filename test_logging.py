from example_script_1 import run as run1
from example_script_2 import run as run2
from example_error_1 import run_error

if __name__ == '__main__':
    run1('This is a test')       # This will log to the file example_script_1.log
    run2('This is another test') # This will log to the file example_script_2.log
    run_error()                  # This will log to the file example_error_1.log
