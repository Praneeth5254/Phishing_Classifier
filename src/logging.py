import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # Generate a log file name based on the current date and time

logs_path = os.path.join(os.getcwd(), "logs") # Get the current working directory and append 'logs' to create the logs directory path

os.makedirs(logs_path, exist_ok=True) # Create the logs directory if it doesn't exist, prevent an error if it already exists

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE) # Define the full path to the log file by combining logs directory path and log file name

logging.basicConfig(
    filename=LOG_FILE_PATH, #everytime a new user comes, it will create a file
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s", # time, line no. where logging call was made, logger's name, log level(INFO, warning, ERROR, Critical, Debug), and messade of error
    level=logging.INFO, #Sets the logging level to INFO, meaning only INFO and more critical messages will be logged.
)