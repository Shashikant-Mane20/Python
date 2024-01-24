first_name="Shashikant"

last_name="Mane"

#string concatenation operator
full_name=first_name+last_name
print(full_name)

#string repetition operator
rep=3*first_name
print(rep)

#length of string
l=len(full_name)
print(l)

#Accessing element from string
s='I am Shashikant'
print(s[0:8:2])
print(s[:-6:-1])
print(s[-1:-6:-1])
print(s[-1:-5:-1])
print(s[5])
print(s[-4])
print(s[-10::1])

#Slicing with the third parameter

s='abc'*3
print(s)
print(s[::3]) #start 0,end length,step 1

#slicin with the third parameter
print(s[1::3])
print(s[:5:3])

#negative Third Prameter
# default steps -1

n="I am Shashikant"

print(n[-1:-5:-1])
print(n[14:10:-1]) #direction is rigth to left

#Reverse a string
print(n[::-1])

str='Shashikant'

for x in str:
    print(x)

#string slicing
    
s='I am Shashikant'
print(s[0:11])

#slicing with third parameter 
#string_variable=[start_index,stop_index,step]

s='I am Shashikant'
print(s[0:8:2])

s='abc'*3
print(s[::3])
print(s[1::3])

#negative third parameter
s='I am Shashikant'
print(s[8:1:-1])
print(s[8:1:-2])
print(s[-7:-14:-2])

s='string'
print(s[5:0:-1])
print(s[1:6:1])

#reverse a string
s='string'
print(s[::-1])
s='I am Shashikant'
print(s[::-1])

#string formatting

name="Shashikant"

print("My name is %s."%name)

city='Thane'

print("My name is %s"%city)

#multiple string formatting

name='Shashikant'
city='Thane'

print('My name is %s and I live in %s'%(name,city))


#str.format() function
name='Shashikant'
city='Thane'

print('My name is {} and I live in {}'.format(name,city)) #using variable name
print('my name is {0} and I live in {1}'.format(name,city))#using index

n='Shashikant'
c='Thane'
print('My name is {name} and I live in {city}'.format(name=n,city=n))

#format specifier like f for float ,b for binary ,d for integer

print("I got {0:f}% in english".format(55.66))
print("I got {0:f}% in english and {1:f}% in spanish".format(55.66,53.33))

print("{0:b}%".format(1))

print('I have {0:d} chocolate'.format(1))

print('I have {0:d} chocolate and {1:d} cakes'.format(1,2))

print('My name is {0:s} and I live in {1:s}'.format('Shashikant','Thane'))

#The length of the values after the decimal point can be controlled.
print("I go {0:.2f}% in English".format(58.679054))

# f-string 
# used to format a string 
# syntac : f'string {object}'

name="Shashikant"

city="Thane"

print(f"My name is {name} I live in {city}.") #f and F is allowed

#call to method of the string is possible

name='Shashikant'
city='Thane'

print(f'My name is {name.upper()} and I live in {city.upper()}')

# For better readability,multiline f-string can be used.

name='Shashikant'
age='21'
gender='Male'
introduction=f'My name is {name}'\
f'I am {age}years old'\
f'and I am {gender}'
print(introduction)

print(f'I am {age}years old {gender} and {introduction}')

# strip() method remove white spaces from leading and trailing 
s="   Hello World   " 
print(s)
print(s.strip())

s="###Hello###"
print(s.strip("#"))
s="Hello"
print(s.strip("He"))

#lstrip()
s="##Hello##"
print(s.lstrip("#"))

#rstrip
s="$$Hello$$"
print(s.rstrip("$"))

#split() method Used to split string into string
s=("I am Shashikant")
print(s.split())

s="I$am$Shashikant"
print(s.split('$',maxsplit=2))
print(s.split('$',maxsplit=1))

#rsplit()
print(s.rsplit('$',maxsplit=1))

#join() method  use to join elements of iterables
l1=['H','e','l','l','o']
print(''.join(l1))
l2=['i','am','Shashikant']
print('-'.join(l2))
print(" ".join(l2))

d={'name':'shashikant','age':'20'}
print(" ".join(d))

# replace()
s="I love strawberry and strawberry"
print(s.replace('strawberry','mango'))
print(s.replace('strawberry','mango',1))

# upper() method
s="shashikant"
print(s.upper())

# lower() method
s="SHASHIKANT"
print(s.lower())

#capitalize()
s='i love India'
print(s.capitalize())

#isupper() It will give true if all alphabates are uppercase else give false
s="SHASHIKANT"
print(s.isupper())
s="shashikant"
print(s.isupper())

#islower() It will give true if all alphabates are lowercase else give false
s="shashikant"
print(s.islower())
s="SHASHIKANT"
print(s.islower())

#isalpha()
s="Shashi"
print(s.isalpha())
s="shashi20"
print(s.isalpha())

#isnumeric()
s="Shashikant"
print(s.isnumeric())
s="1234"
print(s.isnumeric())

# isalnum()
s='shashikant20'
print(s.isalnum())
s="20"
print(s.isalnum())
s="Shashi"
print(s.isalnum())

#count() method
s='I love fruits,fruits make me healthy'
print(s.count('fruits'))
s='I love fruits,Fruits make me healthy'
print(s.count('fruits'))
s='I love fruits,fruits make me healthy'
print(s.count('fruits',0,13))
s='I love fruits,fruits make me healthy'
print(s.count('fruits',0,20))

#find()
s="Python is beautiful language"
print(s.find('b'))
print(s.find('b',0,8)) #-1

# rfind() return the index of last occurence
s="Python is beautiful language"
print(s.rfind('u'))
print(s.rfind('b',0,8)) #-1

#index()
s='Python is beautiful language'
print(s.index('b'))
# print(s.index('b',0,8)) ValueError: substring not found

#rindex() return the index of last occurence
s="python is beautiful language"
print(s.rindex('u'))
# print(s.rindex('b',0,8)) ValueError: substring not found



