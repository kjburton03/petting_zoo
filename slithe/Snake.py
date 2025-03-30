from datetime import date 

class Snake:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.slithes = True
        self.date_added = date.today()
        
smatthew = Snake("smatthew", "slimey")
samanda = Snake("samanda", "two faced serpent")