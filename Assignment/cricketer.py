class cricketer:

    def getdata(self):

        self.name=input("Enter name:")
        self.runs=input("Enter runs:")
        self.wickets=input("Enter wickets:")
        self.matches=input("Enter matches:")
        
        
        
    def display(self):
        print()
        print("Name:",self.name)
        print("Runs:",self.runs)
        print("Wickets:",self.wickets)
        print("Matches:",self.matches)

c1=cricketer()

c1.getdata()
#display information
c1.display()

