# Question: Take positive integer input and tell if it is divisible by 5 or 3 but not divisible by 15.

# user_input=int(input("enter positive integer:"))

# if user_input%15==0:
#     print("divisible by 15")
# else:
#     if user_input%5==0 or user_input%3==0:
#         print("divisible by 5 or 3 but not 15")
#     else:
#         print("neither divisible by 5 or 3")

# Question: Take 3 positive integers input and print the greatest of them (without using multiple condition)

x=int(input("Enter x:"))
y=int(input("Enter y:"))
z=int(input("Enter z:"))

if x>y:
    if x>z:
        print("x is greater than y and z")
    else:
        print("Z is greater than x and y")
else:
    if y>z:
        print("y is greter than x and z")
    else:
        print("z is greter than x and y")
