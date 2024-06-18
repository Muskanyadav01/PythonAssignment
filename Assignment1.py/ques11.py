# Write a python program that generates the first n numbers in the Fibonacci sequence.

#5 -> 1 1 2 3 5

# recursive method
n = int(input("enter your number till which you want to enter your fibonacci series "))
def fibo(n):
    if n <= 0:
        return "the number should be greater than zero"
    elif n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    num = fibo(n-1)
    num.append(num[-1] + num[-2])
    return num

fibo_seq = fibo(n)
print(f"the fibonacci sseries is : {fibo_seq}")

# iterative method

# a = 0
# b = 1
# print("the fibonacci series is : ", end = " ")
# print(a, end = " ")
# print(b, end = " ")
# sum = 0
# for i in range(n-2):
#     sum = a+b
#     print(sum, end = " ")
#     a = b
#     b = sum
    
    

    

