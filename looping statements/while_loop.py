# i=98
# sum=0
# while i<200:
#     i=i+2
#     print(i)
#     sum=sum+i
# print(sum)

#prime number

num=int(input("Enter a number:"))

i=2
while i<num:
    if num%i==0:
        print("Not prime number")
        break
else:
    print("Prime number")
    i=i+1




