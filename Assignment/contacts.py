class contacts:

    def getdata(self):

        self.name=input("Enter name:")
        self.mobile_number=input("Enter mobile number:")
    
        
        
    def display(self):
        print()
        print("Name:",self.name)
        print("Runs:",self.mobile_number)
       
c1=contacts()

c1.getdata()
#display information
c1.display()

