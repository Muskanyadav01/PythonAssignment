# Write a program in python that counts the frequency of each character in a string.
dic = dict()
s = input("enter your string ")
for i in range(len(s)):
    if s[i] in dic:
        dic[s[i]] += 1
    else:
        dic[s[i]] = 1
print(f"frequency of each element in the string is as follows :")
for key,value in dic.items():
    print(f'{key} : {value}')
