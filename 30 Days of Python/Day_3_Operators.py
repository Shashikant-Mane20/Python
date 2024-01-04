# Declare your age as integer variable

age=20

# Declare your height as a float variable

# height=165.5

# Declare a variable that store a complex number

complex=1+2j


# Write a script that prompts the user to enter base and 
# height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).

# base=int(input("Enter base:"))

# height=int(input("Enter height:"))

# area=0.5*base*height

# print("Area of triangle:",area)


# Write a script that prompts the user to enter side a, side b, and side c of the triangle. 
# Calculate the perimeter of the triangle (perimeter = a + b + c).

# a=int(input("Enter side a:"))
# b=int(input("Enter side b:"))
# c=int(input("Enter side c:"))

# perimeter=a+b+c

# print("Perimeter of triangle is",perimeter)


# Get length and width of a rectangle using prompt. 
# Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))

#calculate area of rectangle
# length=int(input("Enter length of reactangle:"))

# width=int(input("Enter width of rectangle:"))

# area=length*width

# print("Area of rectangle is",area)

# #perimeter of rectangle
# perimeter=2*(length+width)

# print("Perimeter of rectangle is",perimeter)


# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) 
# and circumference (c = 2 x pi x r) where pi = 3.14.

# radius=int(input("Enter radius of circle:"))

#calculate area of circle
# pi=3.14
# area=pi*radius*radius

# print("Area of circle is",area)

#circumference of circle

# c=2*pi*radius

# print("Circumference of circle is",c)

# Calculate the slope, x-intercept and y-intercept of y = 2x -2

#Given equation is y= 2x-2 => y= mx+b

m=2
b=-2

x_intercept=-b/m

y_intercept=2*(0)-2

print("Slope is:",m)
print("x_intercept:",x_intercept)
print("y_intercept:",y_intercept)

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.

p=len("python")
d=len("dragon")

print(p==d)

o="on" in "python" and "o" in "dragon"
print(o)

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.

# str="I hope this course is not full of jargon"
# jargon="jargon"
# print(jargon in str)

# There is no 'on' in both dragon and python

print("o" not in "python" and "o" not in "dragon")

# Find the length of the text python and convert the value to float and convert it to string

st="python"
length=len(st)
fl=float(length)
print(type(fl))
string=str(float)
print(type(string))

# Even numbers are divisible by 2 and the remainder is zero.
# How do you check if a number is even or not using python?

# number=int(input("Enter number:"))

# if number%2==0:
#     print("Even number")

# Check if the floor division of 7 by 3 is
# equal to the int converted value of 2.7.
# a=7
# b=3

# f_d=(7//3)
# print(f_d)

# c_v=int(2.7)
# is_equal=(f_d==c_v)

# print(is_equal)

# Check if type of '10' is equal to type of 10

# n=type('10')
# m=10

# print(n==type(m))

# Check if int('9.8') is equal to 10

# p=int('10')==10
# print(p)

# Writ a script that prompts the user to enter hours and 
# rate per hour. Calculate pay of the person?

# hr=int(input('Enter Hourse:'))
# rate=int(input("Enter rate per hour:"))

# pay=hr*rate
# print("Your weekly eatning is:",pay)


# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years

# year=int(input("Enter number of years you have lived:"))

# seconds=31536000*year

# print("You have lived for",seconds,"seconds.")

# Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

# Display the table
for i in range(1, 6):
    row = f"{i} 1 {i} {i**2} {i**3}"
    print(row)


