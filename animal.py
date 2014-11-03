import json


class Animal:

    # "species": ['name 1', 'name 2', ...]
    SPECIES_NAMES = {}

    def __init__(self, species, age, name, gender, weight):
        self.species = species
        self.age = age  # in years, could be float
        self.name = self.set_name(name)
        self.gender = gender
        self.weight = weight

        self.json_data = self.set_json_data_for_species("database.json")
        self.life_expectancy = self.json_data['life_expectancy']
        self.average_weight = self.json_data['average_weight']
        self.weight_age_ratio = self.json_data['weight_age_ratio']
        self.food_weight_ratio = self.json_data['food_weight_ratio']

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

    def set_json_data_for_species(self, json_file):
        file = open(json_file, "r")
        content = file.read()
        file.close()
        return json.loads(content)[self.species]

    def grow(self):
        self.weight = self.weight_age_ratio * (self.age * 12)
        self.age += 1/12  # increase the age with a month

    def eat(self):
        return self.food_weight_ratio * self.weight

    def die(self):
        # in database.json the age is in days, while self.age is in years
        life_expectancy = self.life_expectancy // 356
        chance_of_dying = self.age // life_expectancy
        return chance_of_dying == 1  # if it's above 1 the animal dies
