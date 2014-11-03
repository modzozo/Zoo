import json


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

    def eat(self):
        print("Nom Nom Nom")
        return True

    def die(self):
        file = open("database.json", "r")
        content = file.read()
        file.close()
        # in database.json the age is in days, while self.age is in years
        life_expectancy = json.loads(content)["life_expectancy"] // 356
        chance_of_dying = self.age // life_expectancy
        return chance_of_dying == 1
