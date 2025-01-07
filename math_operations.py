def add(a, b):
    """
    Adds two numbers.

    Example:
    >>> add(3, 5)
    8
    >>> add(-1, 1)
    0
    """
    return a + b


def subtract(a, b):
    """
    Subtracts the second number from the first.

    Example:
    >>> subtract(10, 5)
    5
    >>> subtract(0, 10)
    -10
    """
    return a - b


def multiply(a, b):
    """
    Multiplies two numbers.

    Example:
    >>> multiply(4, 3)
    12
    >>> multiply(0, 5)
    0
    """
    return a * b


def divide(a, b):
    """
    Divides the first number by the second.

    Raises:
        ValueError: If the divisor is zero.

    Examples:
    >>> divide(10, 2)
    5.0
    >>> divide(10, 0)
    Traceback (most recent call last):
    ...
    ValueError: Cannot divide by zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    import doctest

    doctest.testmod()  # Run doctests when this file is executed directly
