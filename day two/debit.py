count=0
for i in range(1,11):
    transaction=input("Enter the transction type (debit or credit)")
    if transaction=="debit":
        count+=1
if count>5:
    print("You are charged with 20rs fee")
else:
    print("You are not charged with any money")
