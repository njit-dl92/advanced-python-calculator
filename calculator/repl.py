# calculator/repl.py

from calculator.plugins import load_plugins

def repl():
    plugins = load_plugins()
    
    print("Welcome to the Advanced Python Calculator REPL")
    while True:
        try:
            # Display prompt and get user input
            command = input("Enter a command (or 'exit' to quit): ").strip()

            if command == 'exit':
                print("Goodbye!")
                break

            # Parse user input for operation and numbers
            operation, a, b = command.split()
            a, b = float(a), float(b)

            # Find the corresponding plugin command
            if operation in plugins:
                result = plugins[operation](a, b)
                print(f"Result: {result}")
            else:
                print(f"Unknown command: {operation}")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    repl()
