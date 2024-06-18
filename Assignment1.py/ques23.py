# Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input.

def FtoC(temp):
    C = (temp-32) * 5/9
    return C

def CtoF(temp):
    F = temp*(9/5) + 32
    return F

print("1. if you want to convert the temp in farehneit press 0 ")
print("2. if you want to convert the temp is celcius press 1 ")
choice = int(input("enter your choice : "))

if choice == 0:
    temp = int(input("enter your temp : "))
    ans  = FtoC(temp)
    print(f"temp in farenheit is {ans}")

elif choice == 1:
    temp = int(input("enter your temp : "))
    ans  = CtoF(temp)
    print(f"temp in celcius is {ans}")

else:
    print(f"you have entered a wrong choice")