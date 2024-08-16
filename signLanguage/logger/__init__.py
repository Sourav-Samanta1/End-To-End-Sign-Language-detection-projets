#This whole  code create the log message with timestamp

import logging  # Importing the logging module for generating log messages.
import os  # Importing the os module for interacting with the operating system.
from datetime import datetime  # Importing datetime for working with dates and times.
from from_root import from_root  # Importing from_root to get the root directory of the project.

# Generate a log file name based on the current date and time.
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the path where the log file will be stored, within a 'log' directory at the project root.
log_path = os.path.join(from_root(), 'log', LOG_FILE)

# Create the 'log' directory if it doesn't already exist.
os.makedirs(log_path, exist_ok=True)

# Define the full path to the log file, including its name.
lOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

# Configure the logging settings.
logging.basicConfig(
    filename=lOG_FILE_PATH,  # Set the log file's path.
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",  # Specify the log message format.
    level=logging.INFO  # Set the logging level to INFO, so only INFO and higher level messages are logged.
)
