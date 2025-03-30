from datetime import date

class Mouse:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walks = True
        
mindy = Mouse("mindy", "quiet")