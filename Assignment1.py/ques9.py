# Write a python program that checks if a substring is present in a given string.
bigs = input("enter your string ")
smalls = input("enter the string you want to search ")
if smalls in bigs:
    print(f"{smalls} is present in {bigs}")
else:
    print(f"{smalls} is not present in {bigs}")
