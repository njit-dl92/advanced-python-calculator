from calculator.logger import logger  # Import the logger

def subtract(a, b):
    result = a - b
    logger.info(f"Subtracting {b} from {a} = {result}")  # Log the subtraction result
    return result
