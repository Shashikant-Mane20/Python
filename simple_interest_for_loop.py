for i in range (1,4):
    p=float(input("Enter Principle for set"+str(i)+":"))
    r=float(input("rate for set"+str(i)+":"))
    t=float(input("time for set"+str(i)+":"))

    si=p*r*t/100
    print("Simple Interest:",si)