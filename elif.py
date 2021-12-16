days = int(input("enter the days:"))
if days==0:
    print("good no fine:")
elif days>=1 and days<=10:
    print("fine amount is:", days*5)
elif days>=10 and days<=20:
    print("fine amount is:", days*10)
    
