
class myModule:
    def __init__(self):
        self.name="My Module"
        self.date_creation="21/02/2024"
        self._creator="Samuel Lunghe"
    def __repr__(self):
        return "Module Name:"+self.name+"\nDate of Creation:"+self.date_creation
    def describe(self):
        print("Name:"+self.name+"\nDate of Creation:"+self.date_creation)
        print("Creator:"+self._creator)
    def funFact(self):
        print("====I was born in 2024===")
    
m=myModule()
m.describe()