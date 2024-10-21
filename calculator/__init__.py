import os

# Define a function to load available plugins dynamically
def load_plugins():
    # Here you can extend logic to discover other plugins dynamically
    from .addition import add
    from .subtraction import subtract
    from .multiplication import multiply  # Import multiply
    from .division import divide          # Import divide

    # Return a dictionary of available plugin commands
    return {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,  # Add multiply to the dictionary
        "divide": divide       # Add divide to the dictionary
    }
