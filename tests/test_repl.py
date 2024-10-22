import unittest
from unittest.mock import patch, MagicMock
from calculator import repl

class TestCalculatorREPL(unittest.TestCase):

    @patch('builtins.input', side_effect=['add 3 5', 'exit'])
    @patch('calculator.plugins.load_plugins')
    def test_add_operation(self, mock_load_plugins, mock_input):
        # Mocking the load_plugins to return a dictionary with an 'add' plugin
        mock_load_plugins.return_value = {'add': MagicMock(return_value=8.0)}
        
        with patch('builtins.print') as mock_print:
            repl.repl()

            # Check if the correct result was printed with consistent float formatting
            mock_print.assert_any_call('Result: 8.0')

    @patch('builtins.input', side_effect=['sub 10 4', 'exit'])
    @patch('calculator.plugins.load_plugins')
    def test_subtract_operation(self, mock_load_plugins, mock_input):
        # Mocking the load_plugins to return a dictionary with a 'sub' plugin
        mock_load_plugins.return_value = {'sub': MagicMock(return_value=6.0)}
        
        with patch('builtins.print') as mock_print:
            repl.repl()

            # Check if the correct result was printed
            mock_print
