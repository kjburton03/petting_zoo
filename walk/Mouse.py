from datetime import date

class Mouse:
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.walks = True
        self.shift = shift
        self.date_added = date.today()
        
        
mindy = Mouse("mindy", "quiet", "clopen bb")
print(mindy)