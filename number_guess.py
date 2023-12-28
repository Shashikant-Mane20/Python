#using random module
import random as r
a=r.randrange(1,100)
print(a)
user_input=int(input("Enter Number between 1 to 100:"))

if user_input==a:
    print("You Won!!!")
else:
    if user_input<a:
        print("To Low")
    else:
        print("To High")


# without random module
# a=19
# print(a)
# user_input=int(input("Enter Number between 1 to 100:"))

# if user_input==a:
#     print("You Won!!!")
# else:
#     if user_input<a:
#         print("To Low")
#     else:
#         print("To High")

