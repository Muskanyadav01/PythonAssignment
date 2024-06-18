# Write a program that asks the user for their name and then prints a greeting message.
name = input("enter your name : ")
print("hello! good morning", name )

# 2nd method
def greet(name):
    print(f"hello! good morning {name}" )
    return
greet(name)