from datetime import date

class Lizard:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.slithes = True
        self.date_added = date.today()

lizzo = Lizard("lizzo", "dotted")
