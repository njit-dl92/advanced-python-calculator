from calculator.core import Calculator
from calculator.plugins import load_plugins

def repl():
    calc = Calculator()
    plugins = load_plugins()

    while True:
        user_input = input(">> ")
        if user_input.lower() in ['exit', 'quit']:
            break
        elif user_input == 'menu':
            print("Available commands:", ", ".join(plugins.keys()))
        else:
            try:
                result = calc.evaluate(user_input)
                print(result)
            except Exception as e:
                print(f"Error: {e}")
