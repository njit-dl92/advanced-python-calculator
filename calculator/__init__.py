import os

# Define a function to load available plugins dynamically
def load_plugins(history):
    # Here you can extend logic to discover other plugins dynamically
    from .addition import add
    from .subtraction import subtract
    from .multiplication import multiply  # Import multiply
    from .division import divide          # Import divide

    # Define the history function
    def show_history(*args):
        if history:
            print("\nHistory of operations:")
            for entry in history:
                print(entry)
        else:
            print("No history available.")

    # Return a dictionary of available plugin commands
    return {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,  # Add multiply to the dictionary
        "divide": divide,      # Add divide to the dictionary
        "history": show_history  # Add history to the dictionary
    }
