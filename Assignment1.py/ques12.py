# Write a python program that calculates the sum of the digits of a given number

num = input("enter your number ")
sum = 0
for i in num:
    sum += int(i)
print(f"the sum of digits of the given number {num} is {sum}")