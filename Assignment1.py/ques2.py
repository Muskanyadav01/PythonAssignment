# Write a python program that checks whether a given number is even or 
# odd

num = int(input("enter your number : "))
# print(f"the number is {'even' if num%2 == 0 else 'odd'}")

if num%2 == 0:
    print("the number is even")
else:
    print("the number is odd")