from datetime import date

class Blowfish:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swims = True
        
baylor = Blowfish("baylor", "bussy")
