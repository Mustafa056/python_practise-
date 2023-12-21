x= int(input("Enter the year: "))

#removes the last two zero..
if x%100==0:
    x=x/100

if x%4==0:
    print(x,"is the leap year")

else:
    print(x,"is not leap year")
