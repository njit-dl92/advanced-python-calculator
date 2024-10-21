# calculator/plugins/__init__.py

import os

# Define a function to load available plugins dynamically
def load_plugins():
    # Here you can extend logic to discover other plugins dynamically
    from .addition import add
    from .subtraction import subtract

    # Return a dictionary of available plugin commands
    return {
        "add": add,
        "subtract": subtract,
    }
