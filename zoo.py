from animal import Animal
import random

class Zoo:
    ANIMAL_INCOME = 60
    MEAT_1KG_PRICE = 4
    GRASS_1KG_PRICE = 2
    PREGNANCY_PERIOD = 6


    def __init__(self, capacity, budget):
        self.animals = []
        self.capacity = capacity
        self.budget = budget



    def accommodate(self, species, age, name, gender, weight):
        if len(self.animals) < self.capacity:
            self.new_animal = Animal(species, age, name, gender, weight)
            self.animals.append(self.new_animal)
        else:
            message ="No capacity now. Try again later"
            raise ValueError(message)


    def get_income(self):
        daily_income = 60 * len(self.animals)
        return daily_income


    def get_outcome(self):
        outcome = 0
        for animal in self.animals:
            if animal.json_species_data.food_type == "meat":
                outcome += animal.eat() * Zoo.MEAT_1KG_PRICE
            else:
                outcome += animal.eat() * Zoo.GRASS_1KG_PRICE

        self.budget -= outcome
        return self.budget

    def dead_animals(self):
        list_dead_animals = []
        for animal in self.animals:
            if animal.die():
                self.animals.remove(animal)
                list_dead_animals.append(animal)
        return list_dead_animals



    def gender_baby(self):
        random_number = random.random()
        if random_number > 0.5:
            return "male"
        return "female"


    def get_female_animals(self):
        female_animals = []
        for animal in self.animals:
            if animal.gender == "female":
                female_animals.append(animal)
        return female_animals


    def reproduce(self,animal1, animal2):

        if animal1.species == animal2.species and animal1.gender != animal2.gender:
            if animal1 in self.get_female_animals() and animal1.non_pregnant_period >= Zoo.PREGNANCY_PERIOD:
                animal1.pregnant_period = 0
                animal1.non_pregnant_period = None

    def newborn_baby(self):
        babies = []
        for animal in self.get_female_animals():
            if animal.pregnant_period == animal.json_species_data['gestation_period']:
                animal.pregnant_period = None
                animal.non_pregnant_period = 0

                baby = Animal(animal.species, 0, animal.set_name(), self.gender_baby(), None)
                babies.append(baby)
                self.animals.append(baby)

        return babies

