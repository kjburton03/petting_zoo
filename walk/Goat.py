from datetime import date

class Goat:
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.walks = True
        self.date_added = date.today()
        
quak = Goat("quak", "rude")


print(quak)
