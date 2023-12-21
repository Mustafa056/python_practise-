x=int(input("Please Enter Number of classes: "))

y=int(input("Please enter number of classes attend: "))

per=y/x*100

print("The percentage rate is",per,'%')

if x<y:
    
    print("You give the wrong information ")

else:

    if per>=75:
        print("You attend the exam")

    else:
        print("You are not eliglible person to attend the exam")









