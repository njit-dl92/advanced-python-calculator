class Calculator:
    def evaluate(self, expression):
        try:
            # Split the expression by spaces to parse it manually
            tokens = expression.split()
            if len(tokens) != 3:
                raise ValueError("Invalid expression format. Use: operand operator operand.")

            left_operand, operator, right_operand = tokens
            
            # Convert operands to float
            left_operand = float(left_operand)
            right_operand = float(right_operand)

            # Handle different operators
            if operator == '+':
                return left_operand + right_operand
            elif operator == '-':
                return left_operand - right_operand
            elif operator == '*':
                return left_operand * right_operand
            elif operator == '/':
                if right_operand == 0:
                    raise ZeroDivisionError("Division by zero is not allowed.")
                return left_operand / right_operand
            else:
                raise ValueError("Unsupported operator. Use +, -, *, or /.")

        except ZeroDivisionError as e:
            raise ZeroDivisionError(str(e))
        except ValueError as e:
            raise ValueError(f"Invalid expression: {e}")
        except Exception as e:
            raise ValueError(f"Invalid expression: {e}")
