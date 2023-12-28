# The ternary operator in Python is a concise way to express conditional expressions. It allows you to assign a
# value to a variable based on a condition in a single line of code.

'''
syntax:
variable=value1 if condtition else value2
'''
#example:


# umbrella="yes" if (raining:=False) else "No"

# print(umbrella)

# Question: Write a program to check if number is odd or even using ternary operator.

number=int(input("Enter a number:"))

result="even" if number%2==0 else "odd"
print(result)