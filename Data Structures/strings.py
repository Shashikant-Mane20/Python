print("Thirty "+"Days "+"of "+"Python")

[print('coding'+' for'+' all')]

company='Coding For All'

print(company)

print('length:',len(company))

print('upper',company.upper())

print('lower',company.lower())

print('capitalize:',company.capitalize())

print('title:',company.title())

print("Swapcase",company.swapcase())

user_input=input("Enter a string:")
modified_str=''
for x in user_input:
  
    if x not in 'aeiouAEIOU':
        modified_str+=x
print('modified_string:',modified_str)