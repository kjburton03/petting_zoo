from datetime import date

class Monkey:
    
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.walks = True
        self.shift = shift
        self.date_added = date.today()

marsella = Monkey("marsella", "new yorker", "all night")


print(marsella)