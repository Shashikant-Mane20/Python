#check weather year is leap year or not

year=int(input("Enter a year:"))

# if year%4==0:
#     if year%100!=0:
#         print(year," is leap year")

#     else:
#         print(year," is not leap year")

# elif year%400==0:
#     if year%100==0:
#          print(year," is leap year")

#     else:
#         print(year," is not leap year")

# else:
#     print(year," is not leap year")

if year%4==0 and year%100!=0:
    print("Leap year")
elif year%400==0 and year%100==0:
    print("Leap year")
else:
    print("Not a leap year")
