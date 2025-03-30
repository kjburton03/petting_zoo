from datetime import date  

class Worm:
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.slithe = True
        self.date_added = date.today()
        
wrizzler = Worm("wrizzler", "grey")