class Animal:

    # "species": ['name 1', 'name 2', ...]
    SPECIES_NAMES = {}

    def __init__(self, species, age, name, gender, weight):
        self.species = species
        self.age = age
        self.name = self.set_name(name)
        self.gender = gender
        self.weight = weight

    def set_name(self, name):
        if self.species not in self.SPECIES_NAMES:
            self.SPECIES_NAMES[self.species] = []
            self.SPECIES_NAMES[self.species].append(name)
            return name  # to initialize self.name
        else:
            if name not in self.SPECIES_NAMES[self.species]:
                self.SPECIES_NAMES[self.species].append(name)
                return name  # to initialize self.name
            else:
                message = ('There is already a {}'
                           ' with that name!').format(self.species)
                raise ValueError(message)

    def grow(self):
        self.weight += 0.500
        self.age += 1

"""
print(Animal.SPECIES_NAMES)
animal1 = Animal("seagull", 3, "Poll", 'male', 1.250)
print(Animal.SPECIES_NAMES)
animal2 = Animal("seagull", 3, "Mark", 'male', 1.250)
print(Animal.SPECIES_NAMES)
"""
