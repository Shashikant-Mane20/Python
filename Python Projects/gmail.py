# email=input("Enter your email:")
# k=0
# i=0
# d=0
# if len(email)>=6:
#     if email[0].isalpha():
#         if("@"in email) and (email.count('@')==1):
#             if (email[-3]==".") ^ (email[-4]=="."):
#                 for x in email:
#                     if x ==x.isspace():
#                         k=1
#                     elif x.isalpha():
#                         if x==x.upper():
#                             i=1
#                     elif x.isdigit():
#                         continue
#                     elif i=="_" or i=="." or i=="@":
#                         continue
#                     else:

#                         d=1
#                 if k==1 or i==1 or d==1:
#                     print("wrong email 5")
#                 else:
#                     print("Right Email")
#             else:
#                 print("wrong email 4")
#         else:
#             print("Wrong email 3")
#     else:
#         print("wrong email,first lettwer shoul be character")
    
# else:
#     print("Wrong email 1")

email=input("Enter your email:")
k,i,d=0,0,0
if len(email)>=6:
    if email[0].isalpha():
        if ('@' in email) and (email.count('@')==1):
            if (email[-3]=='.') ^ (email[-4]=='.'):
                for x in email:
                    if x==x.isspace():
                        k=1
                    elif x.isalpha():
                        if x==x.upper():
                            i=1
                    elif x.isdigit():
                        continue
                    elif x=="_" or x=="." or x=="@":
                        continue
                    else:
                        d=1
                if k==1 or i==1 or d==1:
                    print("Wrong email 5")
                else:
                    print("Right email")
            
            else:
                print("Wrong email 4")
        else:
            print("Wrong email 3")
    else:
        print("Wrong email 2")
else:
    print("Wrong email 1")