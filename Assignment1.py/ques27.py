# Write a program in python that converts a string into a list of its characters

s = input("enter your string ")
st = s.split()
print(f"the list of characters is {list(st[0])}")
print(f"the list of characters is {list(s)}")

ch = []
ch.extend(s)
print(f"the list of characters is {ch}")
