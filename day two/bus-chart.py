rows = 7
columns =4 
for i in range(rows):
    for j in range(columns):
        if (i==2 and j==2) or (i==3 and j==1) or (i==0 and j==0) or (i==4 and j==1) or (i==5 and j==3):
            print('$', end = ' ')
        else:
            print('#', end = ' ')
    print()
