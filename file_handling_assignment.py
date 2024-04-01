# File Creation
def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("First line of text\n")
            file.write("Second line with numbers: 12345\n")
            file.write("Third line with mixed content: Hello, world! 42\n")
        print("File 'my_file.txt' created successfully.")
    except Exception as e:
        print(f"Error occurred while creating the file: {e}")

# File Reading and Display
def read_file():
    try:
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("Content of 'my_file.txt':")
            print(content)
    except FileNotFoundError:
        print("File 'my_file.txt' not found.")
    except PermissionError:
        print("Permission denied to read 'my_file.txt'.")
    except Exception as e:
        print(f"Error occurred while reading the file: {e}")

# File Appending
def append_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Fourth line of text\n")
            file.write("Fifth line with numbers: 67890\n")
            file.write("Sixth line with mixed content: Goodbye, world! 84\n")
        print("Content appended to 'my_file.txt' successfully.")
    except Exception as e:
        print(f"Error occurred while appending to the file: {e}")

if __name__ == "__main__":
    # File Creation
    create_file()
    
    # File Reading and Display
    read_file()
    
    # File Appending
    append_file()
