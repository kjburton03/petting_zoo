from datetime import date

class Shark:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swims = True
        
juju = Shark("juju", "angel")