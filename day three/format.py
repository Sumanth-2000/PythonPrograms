def pattern(string,length):
    for i in range(0,length):
        j=length-1-i 
        for k in range(0,length):
            if k==i or k==j:
                print(string[k],end="")
            else:
                print(end=" ")
        print(" ")   
string=input("Enter the string: ")
length=len(string) 
pattern(string,length) 
