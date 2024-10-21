from calculator.logger import logger  # Import the logger

def divide(a, b):
    try:
        if b == 0:
            logger.error("Attempted to divide by zero.")  # Log the error
            raise ZeroDivisionError("Cannot divide by zero.")
        result = a / b
        logger.info(f"Dividing {a} by {b} = {result}")  # Log the successful division
        return result
    except ZeroDivisionError as e:
        logger.error(f"Division error: {e}")  # Log the exception
        raise  # Re-raise the exception for further handling
