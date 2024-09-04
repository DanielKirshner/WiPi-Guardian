from enum import Enum
import logging
import json
import os

FILE_PATH = os.path.join(os.getcwd(), "config", "config.json")

class JsonKeys(Enum):
    """
    Json keys names as they save inside config.json
    """
    INTERFACE = "INTERFACE"
    WIFI_SSID = "WIFI_SSID"


def get_value_from_json(json_dict: dict, key: str) -> str:
    """
    Get value from json dict according to a key given
    Args:
        json_dict (dict): json file as a dictionary
        key (str): the key that we want to get his value

    Raises:
        json_key_error: key not found

    Returns:
        str: value
    """
    try:
        value = json_dict[key]
    except KeyError as json_key_error:
        logging.error(f"Failed parsing json with the key : {key}")
        raise json_key_error
    
    return value


def get_json_as_dict() -> dict:
    """
    Parsing the json file to a dictionary and returns it.
    Returns:
        dict[str:str] : dictionary of the json keys and values. 
    """
    try:
        with open(FILE_PATH, 'r') as json_file:
            json_dict = json.load(json_file)
    except FileNotFoundError as file_not_found_error:
        logging.error(f"Can not find json config file : {FILE_PATH}")
        raise file_not_found_error
    
    return json_dict
