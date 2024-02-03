# # lists
# # a collection similar or different types of data itemes

# l=[1,2,3,4,5,6,7,8,9,10]
# # start 0 and negative is -1
# #length
# print(len(l))

# print(l)

# #creating a list

# # [] seprated by commas

# e=[]
# print(e) #empty list

# #a list with duplicate items

# num=[1,2,2,3,4,4,5,6,6]
# print(num)

# #creating list with different types of dataitmes

# items=[1,2,'N','Go',3.14]

# #features

# # A list can be duplicate items
# # items in alist are mutable
# # lists can store items of various data types


# # Accessing elements of a single dimensional list
# # list where elements are listed one after the other
# #each element is allocated a unique number called index

# #eg: A list conatainning multiples of 5 up to 20

# my_li=[5,10,15,20]
# print(my_li[0]) #5
# print(my_li[2]) #15

# #negative indexing

# #accessing elements from the last

# print(my_li[-1]) #20
# print(my_li[-2]) #15
# print(my_li[-4])

# #accessing elements of a multidimentional list

# #multi-dimentional list is a list containing another list

# my_list=[[1,2,3],'Shashikant',[4,5,6]]

# print(my_list[2])
# print(my_list[1])
# print(my_list[0][0])

# my_list3=[[1,2,3],[['a','b','c'],5,6]]

# print(my_list3[1][0][1])

# #adding elements to a list

# # append()
# # add item at the end
# # list.append(value)

# lang=['java','c','cpp']
# lang.append('python')
# print(lang)

# #duplicate appened() method to add multiple items

# lang.append('ruby')
# lang.append('javascript')
# lang.append('php')

# print(lang)

# # list as an item can be added
# lang.append(['go','rust','swift'])
# print(lang)


# # insert()
# # add item at specific position

# # list.insert(position,value)
# languages=['python','go']
# languages.insert(0,'python')
# print(languages)

# #extend()

# #a  built in method use to add all items of one list in another list

# # list1.extend(list2)

# list1=['java','c','cpp']
# list2=['javascript','python']

# list1.extend(list2)
# print(list1)

# #input() method
# # user input 
# # user input always converted as string 

# # name=input()
# # ===========================================

# #input() method with a maessage
# # input(message)

# # numer=input("Enter a number")
# # ===============================================
# # typecasting 

# # number=int(input('Enter number'))


# # ============================================

# #return input from the user as a string

# # num=int(input('Enter a number:'))
# # print(num)

# # input a list using loops

# # n=int(input("Enter the number of elements:"))

# # print(n)

# # num1=[]
# # for i in range(n):
# #     x=int(input())
# #     num1.append(x)
# # print(num1)

# # input a list usinng split() method
# # split a string into a list of substring

# # string.split(seprator,maxsplit) 

# sentence='I am John'
# s=sentence.split()
# print(s)


# #input a list using split() method
# #Accepting a list of numbers is easier with split() method

# # lis=input("Enter the numbers")

# # lis=lis.split()
# # print(lis)

# #basic of for loop
# x=[1,2,3,4,5,6,7,8,9]
# for x in range(1,9,2):
#     print(x)

# #accepting a list using split() and for loop
# # n=int(input("Enter number of elements:"))
# # num=input('Enter numbers:')
# # num=num.split()
# # print(num)
# # for i in range(0,n):
# #     num[i]=int(num[i])
# #     print(num)


# #changing list items in python
    
# list=[1,2,3,4]
# list[2]=77
# print(list)

# #changing multiple items

# list[0:2]=[20,40]
# print(list)

# #inserting new item

# list.insert(4,55)
# print(list)

# Declare an empty list
list=[]
print(list)

# Declare a list with more than 5 items

languages=['Python','Javascript','Java','Go','CPP']

# Find the length of your list
print(len(languages))

# Get the first item, the middle item and the last item of the list
print('First Item:',languages[0])
print('Middle Item:',languages[2])
print('Last Item:',languages[-1])

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

list=['Shashikant','21','167.5','Single','India']
print(list)

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

it_companies= ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazone']

# Print the list using print()
print(it_companies)

# Print the number of companies in the list
print('Number of companies in list companies is:',len(it_companies))

# Print the first, middle and last company
print('First Company:',it_companies[0])
print('Middle Company:',it_companies[3])
print('Last Company:',it_companies[6])

# Print the list after modifying one of the companies
# it_companies[2]= 'Adobe'
# print(it_companies)

# Add an IT company to it_companies
#We can do this using append() method
# it_companies.append('Walmart')
# print(it_companies)

# Insert an IT company in the middle of the companies list
# it_companies.insert(4,'HCL')
# print(it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)

# it_companies[2] = it_companies[2].upper()
# print(it_companies)

# Join the it_companies with a string '#;  '
# it_companies = '#;'.join(it_companies)
# print(it_companies)

# Check if a certain company exists in the it_companies list.
# company=input("Enter Company Name:")

# if company in it_companies:
#     print(f"Yes {company} is exist in it_companies")

# else:
#     print(f"NO {company} is not exist in it_companies")

# it_companies.sort()
# print(it_companies)

# Reverse the list in descending order using reverse() method
# it_companies.sort(reverse=True)
# print(it_companies)

# Slice out the first 3 companies from the list
print(it_companies[0:3:1])


# Slice out the last 3 companies from the list
print(it_companies[-1:-4:-1])

# Slice out the middle IT company or companies from the list
# print(it_companies[1:len(it_companies)-1:1])

print(it_companies[3])

# Remove the first IT company from the list
it_companies.remove('Facebook')
print(it_companies)

# Remove the middle IT company or companies from the li
it_companies.remove('Apple')
print(it_companies)

# Remove the last IT company from the list
it_companies.pop()
print(it_companies)

# Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# Destroy the IT companies list
# del it_companies
# print(it_companies)

# Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

print(front_end + back_end)
print()

# for x in back_end:
#     front_end.append(x)
# print(front_end)

front_end.extend(back_end)
print("front_end",front_end)

# After joining the lists in question 26. Copy the joined list 
# and assign it to a variable full_stack. Then insert Python and 
# SQL after Redux.

full_stack= front_end.copy()
print(full_stack)

index=full_stack.index('Redux')

full_stack.insert(index+1,'Python')
full_stack.insert(index+2,'SQL')
print(full_stack)