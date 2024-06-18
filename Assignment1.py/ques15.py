# Write a program that reads data from a CSV file and prints it to the console.

import csv

def read_csv(filename):
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

# Example usage
filename = input("Enter the name of the CSV file: ")
read_csv(filename)
