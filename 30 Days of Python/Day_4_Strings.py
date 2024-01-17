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


