from calculator.plugins import load_plugins

def repl():
    plugins = load_plugins()
    history = []  # List to store history of operations

    print("Welcome to the Advanced Python Calculator REPL")
    while True:
        try:
            # Display prompt and get user input
            command = input("Enter a command (or 'exit' to quit, 'history' to view past operations): ").strip()

            if command == 'exit':
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
            operation, a, b = command.split()
            a, b = float(a), float(b)

            # Find the corresponding plugin command
            if operation in plugins:
                result = plugins[operation](a, b)
                # Store operation in history
                history_entry = f"{operation} {a} {b} = {result}"
                history.append(history_entry)
                print(f"Result: {result}")
            else:
                print(f"Unknown command: {operation}")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    repl()
