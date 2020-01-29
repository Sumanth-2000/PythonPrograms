num=int(input("Enter the initial value: "))
n = int(input('Enter the value of n: '))
count=0
while(count<n):
      for x in range(num,num+1):
          c=0
          for y in range(1,x+1):
              if(x%y==0):
                 c=c+1
          if(c==2):
             print(x)
             count=count+1
      num=num+1
