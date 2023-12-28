n=int(input("Enter four digit number:"))
#n=1234
a=n%10 #4
b=n//10 #123
c=b%10 #3
d=b//10 #12
e=d%10 #2
f=d//10 #1
print(a+c+e+f)