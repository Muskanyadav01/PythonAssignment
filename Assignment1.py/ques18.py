# Write a python program that checks if two strings are anagrams of each other.
st1 = input("enter your first string ").lower()
st2 = input("enter your second string ").lower()

if len(st1) != len(st2):
    print(f" {st1} and {st2} are not anagram of each other since they both have different lengths")

if sorted(st1) == sorted(st2):
    print(f" {st1} and {st2} are anagram of each other")
else:
    print(f" {st1} and {st2} are not anagram of each other")