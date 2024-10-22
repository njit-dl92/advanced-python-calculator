import os
import logging
from calculator.plugins import load_plugins

# Configure logging
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO').upper()
logging.basicConfig(level=LOG_LEVEL, format='%(asctime)s - %(levelname)s - %(message)s')

def repl():
    plugins = load_plugins()
    history = []  # List to store history of operations

    logging.info("Starting the Advanced Python Calculator REPL")
    print("Welcome to the Advanced Python Calculator REPL")
    
    while True:
        try:
            # Display prompt and get user input
            command = input("Enter a command (or 'exit' to quit, 'history' to view past operations): ").strip()

            if command == 'exit':
                logging.info("User exited the calculator.")
                print("Goodbye!")
                break

            # Check if the user wants to view the history
            if command == 'history':
                if history:
                    print("\nHistory of operations:")
                    for entry in history:
                        print(entry)
                else:
                    print("No history available.")
                continue

            # Parse user input for operation and numbers
            parts = command.split()
            if len(parts) != 3:
                logging.warning(f"Invalid command format: {command}")
                print("Invalid command format. Please enter: <operation> <num1> <num2>")
                continue

            operation, a, b = parts
            try:
                a, b = float(a), float(b)
            except ValueError:
                logging.error(f"Invalid number inputs: {a}, {b}")
                print("Error: Inputs must be valid numbers.")
                continue

            # Find the corresponding plugin command
            if operation in plugins:
                result = plugins[operation](a, b)
                # Store operation in history
                history_entry = f"{operation} {a} {b} = {result}"
                history.append(history_entry)
                logging.info(f"Operation performed: {history_entry}")
                print(f"Result: {result}")
            else:
                logging.warning(f"Unknown command: {operation}")
                print(f"Unknown command: {operation}")

        except Exception as e:
            logging.error(f"Error occurred: {e}", exc_info=True)
            print(f"Error: {e}")

if __name__ == "__main__":
    # Determine if the environment is production or development
    ENV = os.getenv('ENV', 'development').lower()

    if ENV == 'production':
        logging.info("Running in production mode")
    else:
        logging.info("Running in development mode")

    repl()
