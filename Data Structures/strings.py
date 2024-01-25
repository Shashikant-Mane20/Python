# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
print("Thirty "+"Days "+"of "+"Python")

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
[print('coding'+' for'+' all')]

# Declare a variable named company and assign it to an initial value "Coding For All".
company='Coding For All'

# Print the variable company using print().
print(company)

# Print the length of the company string using len() method and print().
print('length:',len(company))


print('upper',company.upper())

print('lower',company.lower())

print('capitalize:',company.capitalize())

print('title:',company.title())

print("Swapcase",company.swapcase())

# user_input=input("Enter a string:")
# modified_str=''
# for x in user_input:
  
#     if x not in 'aeiouAEIOU':
#         modified_str+=x
# print('modified_string:',modified_str)

# Cut(slice) out the first word of Coding For All string.
print(company[7::])
# or
words=company.split()
print(words)
print(" ".join(words[1::]))

# Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.find("Coding"))

print(company.index("Coding"))

# Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding','Python'))

# Change Python for Everyone to Python for All using the replace method or other methods.
s='Python for Everyone'
print(s.replace("Everyone","All"))

# Split the string 'Coding For All' using space as the separator (split())
print(company.split(" "))

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
s="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(s.split(","))

# What is the character at index 0 in the string Coding For All.
print(company[0])

# What is the last index of the string Coding For All.
print(company.rindex('l'))
print(company.index('l',13,14))

# What character is at index 10 in "Coding For All" string.
print(company[10])

# Create an acronym or an abbreviation for the name 'Python For Everyone'.
s='Python for Everyone'
l=s.split(" ")
for x in l:
    x=x[0].upper()
    print(x,end="")
print()

# Create an acronym or an abbreviation for the name 'Coding For All'.
s="Coding For All"
l=s.split(" ")
for x in l:
    x=x[0].upper()
    print(x,end="")
print()
# Use index to determine the position of the first occurrence of C in Coding For All.
s="Coding For All"
print(s.index("C"))
# Use index to determine the position of the first occurrence of F in Coding For All.
print(s.index("F"))

# Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(s.rfind("l"))

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'
s= 'You cannot end a sentence with because because because is a conjunction'
print(s.find('because'))
print(s.index('because'))

# Use rindex to find the position of the last occurrence of the word because in 
# the following sentence: 'You cannot end a sentence with because because because is a conjunction'
s='You cannot end a sentence with because because because is a conjunction'
print(s.rindex('because'))

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
s='You cannot end a sentence with because because because is a conjunction'
print(s[31:54:1])

# Find the position of the first occurrence of the word 'because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'
print(s.find('because'))
print(s.index('because'))

# Slice out the phrase 'because because because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'
print(s[31:54:1])

# Does ''Coding For All' start with a substring Coding?
s='Coding For All'
print(s.startswith("Coding"))

# Does 'Coding For All' end with a substring coding?
s='Coding For All'
print(s.startswith("coding"))

# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
s='   Coding For All      ' 
print(s.strip(" "))

# Which one of the following variables return True when we use the method isidentifier():
i='30DaysOfPython' #false
j='thirty_days_of_python' #True

print(i.isidentifier())
print(j.isidentifier())

# The following list contains the names of some of python libraries:
# ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. 
# Join the list with a hash with space string.

l=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("#".join(l))

# Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.

e="I am enjoying this challenge.\nI just wonder what is next."

print(e)

# Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki

tab=" Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki"
print(tab)

# Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
print(f"The are of a circle with radius {radius} is {area} meters square.")

print("The area of a circle with radius {} is {} meters square.".format(radius,area))

print("The area of a circle with radius {0} is {1} meters square.".format(radius,area))

# Make the following using string formatting methods:

print('addition:{}+{}={}'.format(8,6,14))