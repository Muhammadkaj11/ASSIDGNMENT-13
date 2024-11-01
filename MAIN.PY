
def decimal_to_binary(decimal_number):
    if decimal_number < 0:
        return "Invalid input: Please enter a non-negative integer."
    
    binary_number = bin(decimal_number)[2:]  # Use bin() to convert to binary and strip the '0b' prefix
    return binary_number

# Example usage:
decimal_input = int(input("Enter a decimal number: "))
binary_output = decimal_to_binary(decimal_input)
print(f"The binary representation of {decimal_input} is: {binary_output}")
