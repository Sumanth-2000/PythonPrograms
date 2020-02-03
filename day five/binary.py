def find(number):
    if number==0:
        return 0
    else:
        return (number%2+10*find(int(number/2)))
number=int(input("Enter the number: "))
print(find(number))