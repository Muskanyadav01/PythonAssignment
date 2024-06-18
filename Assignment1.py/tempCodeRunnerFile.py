def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return f"Error: File '{filename}' not found."

# Example usage
filename = input("Enter the name of the text file: ")
file_content = read_file(filename)
print(file_content)