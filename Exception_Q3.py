#write a python program that opens a file and handles a FilenotfoundError
#Exception if the file does not exist

def open_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
filename = input("Enter the filename to open: ")
open_file(filename)