# Question: Take input percentage of a student and print the Grade according to marks:
# 1) 81-100 Very Good
# 2) 61-80 Good
# 3) 41-60 Average
# 4) <=40 Fail

# user_input=int(input("enter percentage:"))

# if user_input>80 and user_input<=100:
#     print("Very Good")
# elif user_input>60 and user_input<=80:
#     print("Good")
# elif user_input>40 and user_input<=60:
#     print("Average")
# elif user_input<=40:
#     print("Fail")

# Taking the percentage input from the student
percentage = float(input("Enter the percentage: "))
 
# Determining the grade based on the percentage using elif
if percentage >= 81:
    grade = "Very Good"
elif percentage >= 61:
    grade = "Good"
elif percentage >= 41:
    grade = "Average"
else:
    grade = "Fail"
 
# Printing the grade
print("Grade:", grade)
 