def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"

# Example usage
print(safe_divide(6, 2))
print(safe_divide(10, 0))
print(safe_divide(19, 3))
