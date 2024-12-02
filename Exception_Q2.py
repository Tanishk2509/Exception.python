#write a python program that prompts the user to input an integer and
#raises a ValueError exception if the input is not a valid integer

def get_integer():
    try:
        user_input = input("Enter an integer: ")
        number = int(user_input)  # Try converting the input to an integer
        print(f"You entered: {number}")
    except ValueError:
        raise ValueError("Invalid input. Please enter a valid integer.")

# Example usage
try:
    get_integer()
except ValueError as e:
    print(e)