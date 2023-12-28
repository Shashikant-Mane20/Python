#and and or operator 
# x=10
# y=5

# if x<15 and y<10:
#     print("Both condition is true")
# if x<15 or y>10:
#     print("At least one condition is true")

#Question: Take positive integer input and tell if it is a four digit number or not.

# user_input=int(input("Enter four digit number:"))

# if user_input>999 and user_input<10000:
#     print("Yes",user_input,"is four digit number")
# else:
#     print("Please enter four digit number")

#Question: Take positive integer input and tell if it is divisible by 5 and 3.

#Taking integer input from the user
# user_input=int(input("Enter a positive integer:"))

# #checking user input divisible 5 and 3 or not
# if user_input%5==0 and user_input%3==0:
#     print("Yes it is divisible by 5 and 3")

# else:
#     print("It is not a divisible by 5 and 3")

# Question: Take positive integer input and tell if it is divisible by 5 or 3.

# user_input=int(input("Enter positive integer:"))

# if user_input%5==0 or user%3==0:
#     print("Integer divisible by 5 and 3")
# else:
#     print("Integer is not divisible by 5 and 3")

# Question: Take 3 positive integers input and print the greatest of them.

x=int(input("Enter x:"))
y=int(input("Enter y:"))
z=int(input("Enter z:"))

if x>y and x>z:
    print("x is greater")
elif y>z and y>x:
    print("y is greater")
else:
    print("z is greater")

# if x>y and x>z:
#     print("x is greater")
# if y>z and y>z:
#     print("y is greater")
# if z>x and z>y:
#     print("z is greater")