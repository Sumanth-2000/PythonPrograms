def Repeat(x,num):
    _size = len(x)
    repeated = []
    a=[]
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    for each in range(len(repeated)):
        if (repeated[each]%num)==0:
            a.insert(0,repeated[each])
    return a

n=int(input("Enter the number of elements: "))
mlist=[]
for i in range(0,n):
    m=int(input("Enter the elements: "))
    mlist.insert(1,m)
    i+=1
num=int(input("Enter the number: "))
b=Repeat(mlist,num)
print(b)
