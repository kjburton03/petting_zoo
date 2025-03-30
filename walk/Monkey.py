from datetime import date

class Monkey:
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.walks = True
        self.date_added = date.today()

marsella = Monkey("marsella", "new yorker")


print(marsella)