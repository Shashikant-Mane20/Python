class hockey_player:

    def getdata(self):

        self.name=input("Enter name:")
        self.position=input("Enter position:")
        self.goals=input("Enter no of goals:")
        self.matches=input("Enter matches:")
        
        
        
    def display(self):
        print()
        print("Name:",self.name)
        print("Position:",self.position)
        print("NO of Goals:",self.goals)
        print("Matches:",self.matches)

h1=hockey_player()

h1.getdata()
#display information
h1.display()

