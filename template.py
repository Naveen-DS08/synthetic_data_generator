import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]:%(message)s:")

PROJECT_NAME = "synthetic_data_generator"

list_of_files = [
    f"src/{PROJECT_NAME}/__init__.py",
    f"src/{PROJECT_NAME}/components/__init__.py",
    f"src/{PROJECT_NAME}/utils/__init__.py",
    f"src/{PROJECT_NAME}/utils/common.py",
    f"src/{PROJECT_NAME}/config/__init__.py",
    f"src/{PROJECT_NAME}/config/configuration.py",
    f"src/{PROJECT_NAME}/logging/__init__.py",
    f"src/{PROJECT_NAME}/entity/__init__.py",
    f"src/{PROJECT_NAME}/entity/config_entity.py",
    f"src/{PROJECT_NAME}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "prompt_template.yaml"
    "main.py",
    "Dockerfile",
    "setup.py",
    "research/research.ipynb",
]

# Creating file directory

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # Creating the directory
    if filedir!="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory {filedir} for the file: {filename}")
    
    # Creating the file
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:

            pass
            logging.info(f"Creating an empty file: {filename}")
        
    else:
        logging.info(f"{filename} already exists!")
