# Write a python program that takes a string as input and returns its length.

# method 1
s = input("enter yout string : ")
print(f"length of the string is {len(s)}")

# method 2
c = len(s)
print(f"length of the string is {c}")

# method 3
cnt = 0
i = 0
try:
    while s[i]:
        cnt += 1
        i += 1
except IndexError:
    pass
print(f"length of the string is {cnt}")

