# Write a program in python that checks if a string starts with a given prefix or ends with a given suffix.
s = input("enter your string : ")
suffix = input("enter the suffix you'd like to search for : ")
prefix = input("enter the prefix you'd like to search for : ")
sw = s.startswith(suffix)
ew = s.endswith(prefix)
print(f"the given string {s} startswith the prefix {prefix} {sw} and endswith the suffix {suffix} {ew}")