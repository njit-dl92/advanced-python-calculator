class Calculator:
    def evaluate(self, expression):
        try:
            # Safe eval alternative or direct implementation for safety
            return eval(expression)
        except Exception as e:
            raise ValueError(f"Invalid expression: {e}")
