class lecturer:

    def getdata(self):
        
        self.name=input("Enter name:")
        self.batch=input("Enter batch:")
        self.module_name=input("Enter module name:")

    def display(self):
        print("Name:",self.name)
        print("Batch:",self.batch)
        print("Module name:",self.module_name)

l1=lecturer()

l1.getdata()

l1.display()