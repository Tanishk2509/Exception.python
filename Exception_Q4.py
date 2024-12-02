#write a python program that prompts the user to input two number and 
#raises a TypeError exception if the input are not numerical

def get_numbers():
    try:
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")
        
        # Attempt to convert inputs to floats
        if not (num1.replace('.', '', 1).isdigit() and num2.replace('.', '', 1).isdigit()):
            raise TypeError("Both inputs must be numerical values.")
        
        num1 = float(num1)
        num2 = float(num2)
        print(f"You entered: {num1} and {num2}")
        
    except TypeError as e:
        print(f"Error: {e}")

# Example usage
get_numbers()