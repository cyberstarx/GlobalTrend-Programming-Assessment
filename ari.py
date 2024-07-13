def arithmetic_operation(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        # Check if num2 is not zero to avoid division by zero error
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero!"
    else:
        return "Error: Invalid operator!"

# Example usage:
print(arithmetic_operation(5, 3, '+'))  
print(arithmetic_operation(5, 3, '-'))  
print(arithmetic_operation(5, 3, '*'))  
print(arithmetic_operation(5, 3, '/'))  
print(arithmetic_operation(5, 0, '/'))  
print(arithmetic_operation(5, 3, '%'))  
