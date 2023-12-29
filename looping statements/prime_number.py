#prime number 

num=int(input("Enter any number:"))

for i in range(2,num,1):
    if num%i==0:
        print("It is not a prime number")
        break
else:
    print("It is prime number")
