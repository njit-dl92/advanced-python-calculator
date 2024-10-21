from calculator.logger import logger  # Import the logger

def multiply(a, b):
    result = a * b
    logger.info(f"Multiplying {a} by {b} = {result}")  # Log the multiplication result
    return result
