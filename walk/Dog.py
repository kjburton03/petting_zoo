from datetime import date

class Dog: 
    def __init__(self, name, species):
        self.name = name 
        self.species = species
        self.date_added = date.today()
        self.walk = True
        
kobe_boy = Dog("kobe_boy", "angel from above")

print(kobe_boy)
# 