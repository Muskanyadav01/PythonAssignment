# Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines.

lst = []
while True:
    line = input("enter your line ")
    if not line:
        break
    lst.append(line)
print("All lines are : ")
for line in lst:
    print(line)