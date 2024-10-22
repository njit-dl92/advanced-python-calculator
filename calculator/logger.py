import logging
import os
from dotenv import load_dotenv

load_dotenv()

def setup_logger():
    log_level = os.getenv('LOG_LEVEL', 'INFO').upper()
    logging.basicConfig(filename=os.getenv('LOG_FILE', 'app.log'), level=log_level)
    return logging.getLogger()

logger = setup_logger()

