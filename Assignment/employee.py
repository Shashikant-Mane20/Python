class employee:

    def getdata(self):

        self.name=input("Enter name:")
        self.dept=input("Enter department:")
        self.salary=input("Enter salary:")
        
        
        
    def display(self):
        print()
        print("Name:",self.name)
        print("Department:",self.dept)
        print("Salary:",self.salary)


e1=employee()

e1.getdata()
#display information
e1.display()
