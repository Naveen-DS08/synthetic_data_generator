import os 
import yaml 
import pandas as pd 
import json
from pathlib import Path
from src.synthetic_data_generator.logging.logger import logger

def read_yaml(file_path:Path):
    "Load and return content of a YAML file."

    try:
        with open(file_path, "r") as f:
            content = yaml.safe_load(f)
            logger.info(f"YAML file: {file_path} loaded successfully")
            return content
        
    except FileNotFoundError as e:
        return f"YAML file not found at {file_path}"
    except yaml.YAMLError as e:
        return f"Error parsing YAML file: {e}"
    except Exception as e:
        return f"An unexcepted error found while loading YAML file: {e}"
    
def create_directories(path_of_directories: list,  verbose=True):
    "Create list of directories"
    for path in path_of_directories:
        os.makedirs(path, exist_ok= True)
        if verbose:
            logger.info(f"Created directories at: {path}")

def json_to_csv(json_input:json, output_path:Path):
    """Converts JSON file input to CSV file format"""
    try:
        data = json.loads(json_input)
        if not isinstance(data, list):
            raise ValueError("JSON data must be a list object.")
        df = pd.DataFrame(data)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        df.to_csv(output_path, index=False)
        logger.info(f"JSON file converted to CSV file successfully")
    except json.JSONDecodeError as e:
        return f"JSON decoding error: {e}"
    except ValueError as e:
        return f"Value Error: {e}"
    except Exception as e:
        return f"An unexcepted error occurred during CSV conversion: {e}"