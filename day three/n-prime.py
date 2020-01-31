n = int(input('Enter the value of n: '))
i=1
count=0
while(count<n):
      for x in range(i,i+1):
          c=0
          for y in range(1,x+1):
              if(x%y==0):
                 c=c+1
          if(c==2):
             print(x)
             count=count+1
      i=i+1
