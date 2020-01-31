string=input("Enter the string: ")
pos=int(input("Enter the position of character: "))
num=int(input("Enter the number of characters to remove: "))
for i in range(pos,(pos+num)):
    string=list(string)
    string.pop(i)
str1=""
for ele in string:
    str1+=ele
print(str1)
        
