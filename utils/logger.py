import logging
from datetime import datetime
import os


def configure_logger():
    # Create a logger
    logger = logging.getLogger('api_tests_logger')
    logger.setLevel(logging.DEBUG)

    # Generate a timestamp for the log file
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

    # Create a console handler and set the level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    dir_path = "execution-logs"
    if os.path.isdir(dir_path) is False:
        os.mkdir('execution-logs')

    # Create a file handler and set the level to debug
    log_file_path = f'execution-logs/api_tests_{timestamp}.log'
    fh = logging.FileHandler(log_file_path)
    fh.setLevel(logging.DEBUG)

    # Create a formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger


# Get the logger
logger = configure_logger()
