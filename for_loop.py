"""name = "Meher Nihar Meghla    "

for letter in name:
    print(letter)

mylist = [1,2,3,4,5,6,7,8,9]

for x in mylist:
    print(x**2)

for i in range(1,10):
    print(i)
    

name="Mostofa"

mylist=[i for i in name]

print(mylist)

for i in name:
    mylist.append(i)
print(mylist)"""

mylist2=[i for i in range(1,101) if i%2==1 or i>5]

print(mylist2)