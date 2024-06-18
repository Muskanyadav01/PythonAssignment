# Write a python program that calculates the factorial of a given number

n = int(input("enter the number : "))
# num = 1
# for i in range(1,n+1):
#     num *= i
# print(f"factorial of the number is {num}")

def fact(n):
    if n == 1:
        return 1
    num = fact(n-1)*n
    return num

a = fact(n)
print(f'The factorial of {n} is {a}')