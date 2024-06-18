# Write a python program that takes a list of numbers and returns their sum.

def sum(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum

# lst = [1,2,3,4,5,6,7,8]
# ans = sum(lst)
# print(f"the sum of the given list is {ans}")

n = int(input("enter how many elements you want in the list"))
lst = []
for i in range(n):
    a = int(input("enter your numbers"))
    lst.append(a)
print(lst)

ans = sum(lst)
print(f"the sum of the given list is {ans}")

num = 0
for j in range(len(lst)):
    num += lst[j]
print(f"the sum of the given list is {num}")    
