from datetime import date

class Spider:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.slithes = True
        self.date_added = date.today()
        
spindler = Spider("spindler", "three eye")