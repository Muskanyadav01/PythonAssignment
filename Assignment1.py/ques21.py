#  Write a python program that counts the occurrences of a specific element in a list.
cnt = 0
st = input("enter your string ")
st1 = input("enter the element whose frequency you wish to count : ")
for i in st:
    if i == st1:
        cnt += 1
print(f"frequency of {st1} in {st} is {cnt}")