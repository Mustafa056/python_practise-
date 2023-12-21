class_num = int(input("Total num of class:"))
attent_num= int(input("Number of class you attend:"))

percent = (attent_num/class_num)*100

print(percent)

if percent<75:
    print("You are not eligible for exam")

else:
    print("You are eligible for exam")