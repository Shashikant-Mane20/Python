# import math
# num = int(input("Enter any number:"))

# squareroot=math.sqrt(num)

# print("Sqaure root of"+str(num)+" is :",squareroot)


ui= int(input("Enter 4 digit number:"))

a= ui%10#4

b= ui//10

c=b%10#3

d=b//10

e=d%10#2

f=d//10#1

j=(a**4+c**4+e**4+f**4)
print(j)

if j == ui:
    print("It is a armstrong number")
else:
    print("It is not a armstrong number")


