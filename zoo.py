from animal import Animal
import random

class Zoo:
    ANIMAL_INCOME = 60
    MEAT_1KG_PRICE = 4
    GRASS_1KG_PRICE = 2

    def __init__(self, capacity, budget):
        self.animals = {}
        self.capacity = capacity
        self.budget = budget



    def accommodate(self, species, age, name, gender, weight):
        if len(self.animals) < self.capacity:
            self.new_animal = Animal(species, age, name, gender, weight)
            self.animals.append(self.new_animal)
        else:
            print("No capacity now. Try again later")


    def get_income(self):
        self.budget += 60 * len(self.animals)

    def get_outcome(self):
        outcome = 0
        for animal in self.animals:
            if animal.food_type == "meat":
                outcome += animal.eat() * Zoo.MEAT_1KG_PRICE
            else:
                outcome += animal.eat() * Zoo.GRASS_1KG_PRICE

        self.budget -= outcome
        return self.budget

    def dead_animals(self):

        for animal in self.animals:
            if animal.die() > 1:
                self.animals.remove(animal)

    def gender_baby(self):
        random_number = random.random()
        if random_number > 0.5:
            return "male"
        return "female"
        #TODO
    def reproduce(self, animal1, animal2):
        if animal1.species == animal2.species and animal1.gender != animal2.gender:
            if animal1.gender == "female" and animal1.age - animal1.last_pregnancy >= 6:
                animal1.last_pregnancy = animal1.age
            elif animal2.age - animal2.last_pregnancy >= 6:
                animal2.last_pregnancy = animal2.age
            baby = Animal(animal1.species, 0, animal1.set_name(), self.gender_baby(), None)
            self.animals.accommodate(baby)
        else:
            print("Cannot reproduce. Try again later")

