class Calculator:
    """
    A basic calculator class that supports addition, subtraction, multiplication, division,
    and exponentiation.

    Supports the following methods:

    - __init__(): create a new calculator object.
    - add(a, b): add two numbers and return the result.
    - subtract(a, b): subtract one number from another and return the result.
    - multiply(a, b): multiply two numbers and return the result.
    - divide(a, b): divide one number by another and return the result.
    - exponentiate(a, b): raise a number to a power and return the result.
    """

    def __init__(self):
        """
        Create a new calculator object.
        """
        pass

    def add(self, a, b):
        """
        Add two numbers and return the result.
        """
        return a + b

    def subtract(self, a, b):
        """
        Subtract one number from another and return the result.
        """
        return a - b

    def multiply(self, a, b):
        """
        Multiply two numbers and return the result.
        """
        return a * b

    def divide(self, a, b):
        """
        Divide one number by another and return the result.
        """
        if b == 0:
            raise ValueError("division by zero")
        return a / b

    def exponentiate(self, a, b):
        """
        Raise a number to a power and return the result.
        """
        return a ** b
