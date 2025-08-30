import logging 
import os 
from datetime import datetime 
from src.synthetic_data_generator.utils.common import create_directories

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# create directories
create_directories([log_path], verbose=False)

LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH, 
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO,
)

logger = logging.getLogger("Synthetic-data-generator-logger")
