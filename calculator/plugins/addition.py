from calculator.logger import logger  # Corrected import statement

def add(a, b):
    result = a + b
    logger.info(f"Adding {a} + {b} = {result}")  # Log the addition operation
    return result
