import json


class Animal:

    # "species": ['name 1', 'name 2', ...]
    SPECIES_NAMES = {}

    def __init__(self, species, age_in_months, name, gender, kilos_weight):
        self.json_species_data = self.__set_json_species_data(
            "database.json", species)

        self.species = self.__set_species(species)
        self.age_in_months = age_in_months
        self.name = self.__set_name(name)
        self.gender = self.__set_gender(gender)
        self.kilos_weight = self.__set_kilos_weight(kilos_weight)

        self.non_pregnant_period = None
        self.pregnant_period = None

    def __set_species(self, species):
        if self.json_species_data is not None:
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

    def __set_kilos_weight(self, weight):
        if weight is None:
            return self.json_species_data["newborn_weight"]
        else:
            return weight

    def __set_json_species_data(self, json_file, species):
        file = open(json_file, "r")
        content = file.read()
        file.close()
        if species in json.loads(content):
            return json.loads(content)[species]
        return None

    # depending on simulated time interval, increase
    # animal's weight and age; weight limit is average_weight
    def grow(self, month_time):
        self.age_in_months += month_time
        self.weight_passed_time(month_time)
        self.pregnancy_passed_time(month_time)

    def pregnancy_passed_time(self, month_time):
        if self.species == 'female':
            if self.non_pregnant_period is not None:
                self.pregnant_period += month_time
            else:
                self.non_pregnant_period += month_time

    def weight_passed_time(self, month_time):
        average_weight = self.json_species_data['average_weight']
        if self.kilos_weight < average_weight:
            c = self.json_species_data['weight_age_ratio'] * self.age_in_months
            self.kilos_weight = min(c, average_weight)

    # return how many kilos the animal should consume
    def eat(self):
        return self.json_species_data['food_weight_ratio'] * self.kilos_weight

    # *** not really --> ranomize it...
    # if chance of dying is above 1, the animal dies
    def die(self):
        # self.age is in months so roughly turn it to days
        chance_of_dying = self.age_in_months * 30 // self.json_species_data['life_expectancy']
        if chance_of_dying >= 1:
            self.SPECIES_NAMES[self.species].remove(self.name)
        return chance_of_dying >= 1

    def __str__(self):
        return "{}: {}, {} months, {} kilos".format(self.name,
                                                    self.species,
                                                    self.age_in_months,
                                                    self.kilos_weight)
