# File: add_numbers.py
import sys

def add_numbers(num1, num2, num3):
    return num1 + num2 + num3
 
def main():
    # Check if correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Command line: python add_numbers.py <number1> <number2> <number3>")
        sys.exit(1)

    try:
        # Convert command-line arguments to floats
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        num3 = float(sys.argv[3])
        
        # Calculate sum
        result = add_numbers(num1, num2, num3)
        
        # Print result
        print(f"{num1} + {num2} + {num3} = {result}")
        
    except ValueError:
        print("Error: Please provide valid numbers")
        sys.exit(1)

if __name__ == "__main__":
    main()
