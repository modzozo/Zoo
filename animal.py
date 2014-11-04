import json


class Animal:

    # "species": ['name 1', 'name 2', ...]
    SPECIES_NAMES = {}

    def __init__(self, species, age, name, gender, weight=None):
        self.__json_data = self.__set_json_data_for_species(
            "database.json", species)

        self.species = self.__set_species(species)
        self.age = age  # in months because of the requirements
        self.name = self.__set_name(name)
        self.gender = self.__set_gender(gender)
        self.newborn_weight = self.__json_data['newborn_weight']
        self.weight = self.__set_weight(weight)  # in kilos

        self.life_expectancy = self.__json_data['life_expectancy']  # in days
        self.average_weight = self.__json_data['average_weight']
        self.weight_age_ratio = self.__json_data['age']  # here key should be
                                                         # 'weight_age_ratio'
                                                         # but in our *.json
                                                         # is only 'age'
        self.food_weight_ratio = self.__json_data['food_weight_ratio']

        self.food_type = self.__json_data['food_type']  # here could be
                                                        # made checks
                                                        # but are missing
                                                        # for now
        self.gestation_period = self.__json_data['gestation_period']

    def __set_species(self, species):
        if self.__json_data is not None:
            return species
        else:
            message = "Our database has no info for this species."
            raise ValueError(message)

    def __set_name(self, name):
        if self.species not in self.SPECIES_NAMES:
            self.SPECIES_NAMES[self.species] = []
            self.SPECIES_NAMES[self.species].append(name)
            return name
        else:
            if name not in self.SPECIES_NAMES[self.species]:
                self.SPECIES_NAMES[self.species].append(name)
                return name
            else:
                message = ('There is already a {}'
                           ' with that name!').format(self.species)
                raise ValueError(message)

    def __set_gender(self, gender):
        if gender in ['male', 'female', 'hemafrodit']:
            return gender
        else:
            message = "No such gender exists!"
            raise ValueError(message)

    def __set_weight(self, weight):
        if weight is None:
            return self.newborn_weight
        else:
            return weight

    def __set_json_data_for_species(self, json_file, species):
        file = open(json_file, "r")
        content = file.read()
        file.close()
        if species in json.loads(content):
            return json.loads(content)[species]
        return None

    # depending on simulated time interval, increase
    # animal's weight and age; weight limit is average_weight
    def grow(self, month_time):
        self.age += month_time
        if self.weight < self.average_weight:
            self.weight = min(self.weight_age_ratio * self.age,
                              self.average_weight)

    # return how many kilos the animal should consume
    def eat(self):
        return self.food_weight_ratio * self.weight

    # if chance of dying is above 1, the animal dies
    def die(self):
        # self.age is in months so roughly turn it to days
        chance_of_dying = self.age * 30 // self.life_expectancy
        if chance_of_dying >= 1:
            self.SPECIES_NAMES[self.species].remove(self.name)  # free name for
                                                                # further use
        return chance_of_dying >= 1

    def __str__(self):
        return "{}: {}, {} months, {} kilos".format(self.name,
                                                    self.species,
                                                    self.age,
                                                    self.weight)
