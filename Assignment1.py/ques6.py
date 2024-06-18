# Write a program that reads the content of a text file and prints it to the console.

# try:
#     with open(file1.txt,'r') as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print(f'file you aree searching for not found')

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return f"Error: File '{filename}' not found."

filename = input("Enter the name of the text file: ")
file_content = read_file(filename)
print(file_content)
