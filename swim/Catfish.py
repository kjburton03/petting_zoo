from datetime import date 

class Catfish:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swims = True
        
kimberlina = Catfish("kimberlina", "one of a kind bb")