num1 = int(input("Enter Number1:"))
num2 = int(input("Enter Number2:"))

operator=input("Enter operator")

match operator:
    case "+":
        print("sum:",num1+num2)

    case "-":
        print("diff:",num1-num2)

    case "*":
        print("product:",num1*num2)

    case "/":
        print("qutiont:",num1/num2)