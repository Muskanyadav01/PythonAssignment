# Write a python program that removes all punctuation from a given string.

st = input("enter your string : ")
ans = ""
for i in st:
    if i.isalnum():
        ans += i

print(f"string without punctuation marks is {ans}")