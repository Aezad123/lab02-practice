# math_tools .py

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def is_even(n):
    return n % 2 == 0

def subtract(a, b):
    return a - b

def max_of_three(a, b, c):
    max_val = a
    if b > max_val:
        max_val = b
    if c > max_val:
        max_val = c
    return max_val

def is_palindrome(s):
    s = s.replace(" ", "")
    return s == "".join(reversed(s))

def find_min(numbers):
    if len(numbers) == 0:
        raise ValueError("List cannot be empty")

    min_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
    return min_val

def remove_duplicates(items):
    a = []
    for item in items:
        if item not in a:
            a.append(item)
    return a