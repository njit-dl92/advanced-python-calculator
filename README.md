# Advanced Python Calculator

DEMO Link : https://youtu.be/byFWwvx2IiQ 

Below are the project implementation details:

Created a .env file to configure environment variables dynamically, especially for logging levels or file paths.

Implemented a simple REPL interface in repl.py using a while loop that reads user input, evaluates expressions, and prints results.
The interface  supports basic operations (Add, Subtract, Multiply, Divide) and history command to show history as well as dynamic loading of plugins.

Implemented core functionality in core.py where arithmetic operations are handled, and the result is returned.

Implemented a dynamic plugin system in the plugins folder. Each plugin should be loaded dynamically at runtime and should provide additional operations.

Used Pandas to manage the history of all calculations, enabling users to save/load history from a CSV file.

Implemented methods in history_manager.py for saving/loading history.

Implemented logging functionality in logger.py with different logging levels (INFO, ERROR, etc.) and used environment variables for dynamic configuration.

Used below design patterns:

Facade Pattern: Simplify the interface to Pandas in history_manager.py.

Command Pattern: Organize REPL commands.

Factory Pattern: Use factories to create calculator instances or plugin loaders.

Singleton Pattern: Ensure logging configuration is instantiated only once.

Wrote tests in the tests folder for each functionality.

Used pytest-cov to measure test coverage.

Used a .github/workflows/python-app.yml for continuous integration.
Sucessful execution of Actions can be obsered in : [https://github.com/njit-dl92/advanced-python-calculator ](https://github.com/njit-dl92/advanced-python-calculator/actions) 

Git link for complete development: https://github.com/njit-dl92/advanced-python-calculator 

