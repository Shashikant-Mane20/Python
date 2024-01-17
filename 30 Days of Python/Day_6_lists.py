# lists
# a collection similar or different types of data itemes

l=[1,2,3,4,5,6,7,8,9,10]
# start 0 and negative is -1
#length
print(len(l))

print(l)

#creating a list

# [] seprated by commas

e=[]
print(e) #empty list

#a list with duplicate items

num=[1,2,2,3,4,4,5,6,6]
print(num)

#creating list with different types of dataitmes

items=[1,2,'N','Go',3.14]

#features

# A list can be duplicate items
# items in alist are mutable
# lists can store items of various data types


# Accessing elements of a single dimensional list
# list where elements are listed one after the other
#each element is allocated a unique number called index

#eg: A list conatainning multiples of 5 up to 20

my_li=[5,10,15,20]
print(my_li[0]) #5
print(my_li[2]) #15

#negative indexing

#accessing elements from the last

print(my_li[-1]) #20
print(my_li[-2]) #15
print(my_li[-4])

#accessing elements of a multidimentional list

#multi-dimentional list is a list containing another list

my_list=[[1,2,3],'Shashikant',[4,5,6]]

print(my_list[2])
print(my_list[1])
print(my_list[0][0])

my_list3=[[1,2,3],[['a','b','c'],5,6]]

print(my_list3[1][0][1])

#adding elements to a list

# append()
# add item at the end
# list.append(value)

lang=['java','c','cpp']
lang.append('python')
print(lang)

#duplicate appened() method to add multiple items

lang.append('ruby')
lang.append('javascript')
lang.append('php')

print(lang)

# list as an item can be added
lang.append(['go','rust','swift'])
print(lang)


# insert()
# add item at specific position

# list.insert(position,value)
languages=['python','go']
languages.insert(0,'python')
print(languages)

#extend()

#a  built in method use to add all items of one list in another list

# list1.extend(list2)

list1=['java','c','cpp']
list2=['javascript','python']

list1.extend(list2)
print(list1)

#input() method
# user input 
# user input always converted as string 

# name=input()
# ===========================================

#input() method with a maessage
# input(message)

# numer=input("Enter a number")
# ===============================================
# typecasting 

# number=int(input('Enter number'))


# ============================================

#return input from the user as a string

# num=int(input('Enter a number:'))
# print(num)

# input a list using loops

# n=int(input("Enter the number of elements:"))

# print(n)

# num1=[]
# for i in range(n):
#     x=int(input())
#     num1.append(x)
# print(num1)

# input a list usinng split() method
# split a string into a list of substring

# string.split(seprator,maxsplit) 

sentence='I am John'
s=sentence.split()
print(s)


#input a list using split() method
#Accepting a list of numbers is easier with split() method

# lis=input("Enter the numbers")

# lis=lis.split()
# print(lis)

#basic of for loop
x=[1,2,3,4,5,6,7,8,9]
for x in range(1,9,2):
    print(x)

#accepting a list using split() and for loop
# n=int(input("Enter number of elements:"))
# num=input('Enter numbers:')
# num=num.split()
# print(num)
# for i in range(0,n):
#     num[i]=int(num[i])
#     print(num)


#changing list items in python
    
list=[1,2,3,4]
list[2]=77
print(list)

#changing multiple items

list[0:2]=[20,40]
print(list)

#inserting new item

list.insert(4,55)
print(list)
