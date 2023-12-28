#Variables in Python
# a=10
# b="Shashikant"
# pi=3.14
# print(a)
# print(b)
# print(pi)

#Variables Types:
intx=5 #in python we no need to assign type of variable
a= 10 #int
Pi= 3.14 #float
name= "Shashikant" #string
i_am_boy=True #boolean
i_am_girl=False #boolean
print(type(intx))
print(type(a))
print(type(Pi))
print(type(name))
print(type(i_am_boy))
print(type(i_am_girl))

#Variable Concatination
first_name="Shashikant"
last_name="Mane"
#full_name=(first_name+last_name)
full_name=(first_name+" "+last_name) #if we wanted to add space between strings add "" with +

print(full_name)

#variable Reassignment
a=10
print(a) #Output:10

a="Hello World"
print(a) #Output:Hello World

#multiple Assignments
x,y,z=10,20,30
print(str(x)+" "+str(y)+" "+str(z)) #for int concatenation use to convert int into string using str()

#Variable Scope
global_var="global_varable"
def my_function():
    local_var="local_variable"

    print(local_var) #local variable accessible in the function only
    print(global_var)

my_function()
print(global_var) #global vaiable accessible any where in the program
