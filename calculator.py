def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division durch Null ist nicht erlaubt")
    return a / b

def is_even(n):
    return n % 2 == 0
