# Write a program that takes a string input from the user and writes it to a text file

st = input("enter your string ")
file = open("file.txt","x")
file.write(st)
file.close()

file1 = open("file1.txt","w")
file1.write(st)
file.close()