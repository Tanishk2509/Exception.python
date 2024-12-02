#write a python program to handle a ZeroDivisionError exception when dividing a number by zero.?

def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        print(f"The result of dividing {num1} by {num2} is: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
num1 = float(input("Enter the numerator: "))
num2 = float(input("Enter the denominator: "))

divide_numbers(num1, num2)