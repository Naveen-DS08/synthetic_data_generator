import streamlit.web.cli as stcli
from src.synthetic_data_generator.logging.logger import logger
import sys 

def main():
    "Main entry pointof the application"
    logger.info("Starting Synthetic Data Generator Application")
    sys.argv = ["streamlit", "run", "app.py"]    # sys.argu is used to run streamlit from script
    stcli.main()

if __name__== "__main__":
    main()