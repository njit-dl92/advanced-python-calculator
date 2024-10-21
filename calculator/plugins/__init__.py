import os

# Define a function to load available plugins dynamically
def load_plugins():
    """Dynamically load all calculator plugins and return their functions."""
    
    from .addition import add
    from .subtraction import subtract
    from .multiplication import multiply
    from .division import divide

    # Return a dictionary of available plugin commands
    return {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }
