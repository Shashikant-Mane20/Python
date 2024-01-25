'''
In Python, a raw string is a special type of string that allows you to include backslashes (\)
 without interpreting them as escape sequences. In this article, we will see how to take care of a backslash
 combined with certain alphabet forms literal characters which can change the entire meaning of the string using Python.
'''
print(r"My \n self")
print(R"we use \t for indentation in python")

name="Shashi"
name=name+"kant"
print(name)


original_string = "Hello   World"
new_string = "".join(original_string.split())
print(new_string)

print(original_string.replace("   ",''))


s='I am monkey,I am,I am'
print(s.replace("I","Me",2))