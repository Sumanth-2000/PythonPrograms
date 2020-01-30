i=1
while i<21:
    if i==1 or i==3 or i==5 or i==2 or i==6 or i==10 or i==14:
        print("position ",i," is already hired")
        i+=1
    else:
        skill=input("Enter your skill: ")
        if skill=="java" or skill=="python" or skill=="javascript":
            print("You are hired for ",i," position")
            i+=1
        else:
            print("Better luck next time")

    
