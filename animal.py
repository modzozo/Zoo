import json
from random import uniform
#from zoo import Zoo


class Animal:

    # "species": ['name 1', 'name 2', ...]
    SPECIES_NAMES = {}

    PREGNANCY_PERIOD = 6
    # PREGNANCY_PERIOD = Zoo.PREGNANCY_PERIOD
    DAYS_APPROXIMATION = 30

    def __init__(self, species, age_in_months, name,
                 gender, kilos_weight=None):
        self.json_species_data = self.__set_json_species_data(
            "database.json", species)

        self.species = self.__set_species(species)
        self.age_in_months = age_in_months
        self.name = self.__set_name(name)
        self.gender = self.__set_gender(gender)
        self.kilos_weight = self.__set_kilos_weight(kilos_weight)

        self.non_pregnant_period = Animal.PREGNANCY_PERIOD
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

    def grow(self, month_time):
        self.age_in_months += month_time
        self.__weight_simulated_time(month_time)
        self.__pregnancy_simulated_time(month_time)

    def __weight_simulated_time(self, month_time):
        average_weight = self.json_species_data['average_weight']
        if self.kilos_weight < average_weight:
            weight_age_ratio = self.json_species_data['weight_age_ratio']
            weight_increased = weight_age_ratio * self.age_in_months
            self.kilos_weight = min(weight_increased, average_weight)

    # not accurate for simulated time long enough for more than one pregnancy
    # but in such case babies check problem would appear...
    def __pregnancy_simulated_time(self, month_time):
        if self.gender == 'female':
            if self.pregnant_period is not None:
                pregnant_period_increased = self.pregnant_period + month_time
                gestation_limit = self.json_species_data['gestation_period']
                self.pregnant_period = min(pregnant_period_increased,
                                           gestation_limit)
            else:
                non_pregnant_increased = self.non_pregnant_period + month_time
                non_pregnancy_limit = Animal.PREGNANCY_PERIOD
                self.non_pregnant_period = min(non_pregnant_increased,
                                               non_pregnancy_limit)

    def eat(self):
        return self.json_species_data['food_weight_ratio'] * self.kilos_weight

    def die(self):
        age_in_days = self.age_in_months * Animal.DAYS_APPROXIMATION
        life_expectancy = self.json_species_data['life_expectancy']
        chance_of_dying = age_in_days / life_expectancy

        death_arbiter = uniform(0, 2)

        if death_arbiter < chance_of_dying:
            self.SPECIES_NAMES[self.species].remove(self.name)
            return True
        else:
            return False

    def set_name(self):
        get_name = input("\nHow to name the baby?: ")
        return get_name

    def __str__(self):
        return "{}: {}, {} months, {} kilos".format(self.name,
                                                    self.species,
                                                    self.age_in_months,
                                                    self.kilos_weight)
