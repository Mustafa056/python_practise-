x = int(input("The first number is:"))

y = int(input("The second number is:"))

z = int(input("The third number is:"))

if x>y and x>z:
    print(x, "is the biggest number")

elif y>x and y>z:
    print(y, "is the biggest number")

else:
    print(z, "is the biggest number")