'''Loan app
registration charges for land based on
Square feet
Pincode'''

land=float(input("Enter the land size in sq.feet: "))
pincode=int(input("Enter the pincode of ur area: "))
amountForSqFeet=500
if pincode<=10:
    print("U need to pay 5% extra for registration")
    amount=(amountForSqFeet*land)+(((amountForSqFeet*land)*5)/100)
    print("The Total amount for land ",amount)
elif pincode>10 and pincode<=20:
    print("U need to pay 10% extra for registration")
    amount=(amountForSqFeet*land)+(((amountForSqFeet*land)*10)/100)
    print("The Total amount for land ",amount)
elif pincode>20 and pincode<=30:
    print("U need to pay 15% extra for registration")
    amount=(amountForSqFeet*land)+(((amountForSqFeet*land)*15)/100)
    print("The Total amount for land ",amount)
else:
    print("U need to pay 20% extra for registration")
    amount=(amountForSqFeet*land)+(((amountForSqFeet*land)*20)/100)
    print("The Total amount for land ",amount)
