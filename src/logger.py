from datetime import datetime
import logging
import sys
import os


def timestamp_now() -> str:
    """
    Get current timestamp for the log file name.

    Returns:
        str: current timestamp as a valid string for filename
    """
    return str(datetime.now().strftime(r"%d-%m-%Y-%H-%M-%S"))


def create_logger_folder(log_dir_path: str) -> None:
    """
    Check if the logger folder exists, otherwise it creates one.

    Args:
        log_dir_path (str): full path to logs folder.
    """
    if not os.path.exists(log_dir_path):
        os.makedirs(log_dir_path)


def init() -> None:
    """
    Initialize the logger.
    - creates logger dir if it does not exists.
    - creates new log file with the current timestamp.
    - Config the logger to save all messages to the log file.
    - Config the logger to print all messages to console (stdout)
    """
    log_dir_path = os.path.join(os.getcwd(), "logs")
    log_file_path = os.path.join(log_dir_path, f"{timestamp_now()}.log") 
    create_logger_folder(log_dir_path)

    logging.basicConfig(level=logging.INFO, 
                    filename=log_file_path,
                    filemode='w',
                    format=f"%(asctime)s - %(levelname)s - %(message)s")
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
