# Get user input using input(“Enter your age: ”). If user is 18 or older, 
# give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years

# age=int(input("Enter your age:"))

# if age>=18:
#     print("You are old enough to derive")

# else:
#     print("wait for missing amout of years")

# my_age=20

# your_age=int(input("Enter your age:"))
# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.
# if your_age==my_age:
#     print("We are same age")
# else:
#     if your_age>my_age:
#         diff=your_age-my_age
#         print("you are",diff,"years older than me.")
#     else:
#         diff1=my_age-your_age
#         print("You are",diff1,"years younger than me")

# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. 
# a=int(input("Enter number 1:"))
# b=int(input("Enter number 2:"))

# if a>b:
#     print(a,"is greater than",b)

# else:
#     print(b,"is greater than",a)

# grade=int(input("Enter student grade:"))

# Write a code which gives grade to students according to theirs scores:
# if grade<=100 and grade>=80:
#     print("A grade")
# elif grade>=70 and grade<=89:
#     print("B grade")
# elif grade>=60 and grade<=69:
#     print("C grade")
# elif grade>=50 and grade<=59:
#     print("D grade")
# elif grade>=0 and grade<=49:
#     print("F grade")


# month=input("Enter a month to check season:")

# if month=="September" or month=="October" or month=="November":
#     print("Autumn")
# elif month=="Dacember" or month=="January" or month=="February":
#     print("Winter")
# elif month=="March" or month=="April" or month=="May":
#     print("Spring")
# else:
#     print("Summer")

#match case

num1=int(input("Enter number1:"))
num2=int(input("Enter number2:"))

operator=input("Enter Operator:")

match operator:
    case"+":
        print("sum:",num1+num2)
    case"-":
        print("diff:",num1-num2)
    case"*":
        print("product:",num1*num2)
    case"/":
        print("quotient:",num1/num2)
    case _:
        print("Please enter right operator")