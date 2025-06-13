import os
import sys
import logging

# 1. Define the log format
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# 2. Define where the log file should be saved
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")

# 3. Create the directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)

# 4. Configure the logging system
logging.basicConfig(
    level=logging.INFO,  # Set log level
    format=logging_str,  # Use the custom format
    handlers=[
        logging.FileHandler(log_filepath),  # Save logs to a file
        logging.StreamHandler(sys.stdout)   # Show logs in terminal
    ]
)

# 5. Create a logger object
logger = logging.getLogger("mlProjectLogger")

# 6. Log some messages

#logger.info("This is an INFO message")
#logger.warning("This is a WARNING message")
#logger.error("This is an ERROR message")
