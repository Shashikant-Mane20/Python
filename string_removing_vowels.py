user_input=input("Enter a string:")
modified_str=''
for x in user_input:
  
    if x not in 'aeiouAEIOU':
        modified_str+=x
print('modified_string:',modified_str)