from datetime import date

class Dragon:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.slithes = True
        self.date_added = date.today()
        
drago = Dragon("drago", "street walker")

print(drago)
