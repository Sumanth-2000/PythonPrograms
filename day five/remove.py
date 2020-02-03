def Repeat(x):
    _size = len(x)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    a=repeated[0]
    for each in range(1,len(repeated)):
        a ^= repeated[each]
    return a


# Driver Code
n=int(input("Enter the number of elements: "))
mlist=[]
for i in range(0,n):
    m=int(input("Enter the elements: "))
    mlist.insert(1,m)
    i+=1
b=Repeat(mlist)
mlist= list(dict.fromkeys(mlist))
print(mlist)
mlist.append(b)
print(mlist)


# Driver Code
