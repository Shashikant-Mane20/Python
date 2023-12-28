#Arithmetic Operators
a=10
b=12
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b) # true division==>returns quotient
print(a%b) # modulus==>returns remainder
print(a**b) #exponent

#Assignment Operator
# x=10 # =
# x+=5 # +=
# x-=5 # -=
# x*=5 # *=
# x/=5 # /=
# x//=5 # //=
# x%=5 # %=
# x**5 # **=
# print(x)
n=20
n+=10
print(n)
a=20
a-=10
print(a)
b=20
b*=2
print(b)
c=30
c/=6
print(c)

#comparison Operator
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
# The == operator checks if two values are equal.
# The != operator checks if two values are not equal.
# The > operator checks if the value on the left is greater than the value on the right.
# The < operator checks if the value on the left is less than the value on the right.
# The >= operator checks if the value on the left is greater than or equal to the value on the right.
# The <= operator checks if the value on the left is less than or equal to the value on the right

#logical operators
# and operator
# Returns True if both conditions are true.
x=5
y=10
result1=x<10 and y>5
print("x<10 and y>5",result1)

# or operator
# Returns True if at least one condition is true.
m=7
n=3
result2=m<5 or n>10
print("m<5 or n>10",result2)

# not Operator
# Returns True if the condition is false, and vice versa.
p=True
result3=not p
print(result3)

#membership Operator
#in operator
#Returns True if a value is found in the sequence.
list=[1,2,3,4,5]
l_result=3 in list
print("3 in list:",l_result) #O/p:True

l_result2=6 in list
print("6 in list",l_result2)

#not in operator
#Returns True if a value is not found in the sequence.
string="Hello World"
s_result="Python" not in string
print("Python not in string",s_result) #O/p:True

# identity operators
#is operator
#Returns True if the operands are the same object (refer to the same memory location).
s = [1, 2, 3]
t = [1, 2, 3]
# d = s

result1 = s is t
print("s is t:", result1)  # Output: False
# This is because even though the contents of s and t are the same, they are distinct objects in memory. 
# If you want to check if the contents of the lists are equal, you should use the equality operator (==) i
# nstead of the identity operator (is):

result=s==t
print("s==t",result)

# result2 = s is d
# print("s is d:", result2)  # Output: True

s=10
t=10
print("s is t",s is t)

a = 10
b = 3
 
# Bitwise Operators
print("Bitwise AND:", a & b)


