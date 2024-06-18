#  Write a program that copies the contents of one text file to another

def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as destination:
                # Read the content of the source file
                content = source.read()
                # Write the content to the destination file
                destination.write(content)
        print(f"Content copied from '{source_file}' to '{destination_file}' successfully.")
    except FileNotFoundError:
        print(f"Error: File '{source_file}' not found.")

source_filename = input("Enter the name of the source file: ")
destination_filename = input("Enter the name of the destination file: ")
copy_file(source_filename, destination_filename)
