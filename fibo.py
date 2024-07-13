def fibonacci(n):
    # Base cases
    if n <= 0:
        return "Input should be a positive integer"
    elif n == 1 or n == 2:
        return 1
    
    # Recursive case
    return fibonacci(n-1) + fibonacci(n-2)

# Example usage
for i in range(1, 11):
    print(f"Fibonacci({i}) = {fibonacci(i)}")

