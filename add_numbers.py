# File: add_numbers.py
import sys

def add_numbers(num1, num2):
    """Add two numbers and return their sum."""
    return num1 + num2

def main():
    # Check if correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python add_numbers.py <number1> <number2>")
        sys.exit(1)

    try:
        # Convert command-line arguments to floats
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        
        # Calculate sum
        result = add_numbers(num1, num2)
        
        # Print result
        print(f"{num1} + {num2} = {result}")
        
    except ValueError:
        print("Error: Please provide valid numbers")
        sys.exit(1)

if __name__ == "__main__":
    main()