from animal import Animal
import random

class Zoo:
    def __init__(self, animals, capacity, budget):
        self.animals = set()
        self.capacity = capacity
        self.budget = budget


    def accommodate(self, new_animal):
        self.animals.add(new_animal)

    def get_income(self, num_animals):
        self.budget += 60 * num_animals

    def get_outcome(self, meat, grass):
        meat = 0
        grass = 0
        for animal in self.animals:
            grass += animal.grass_eaten
            meat += animal.meat_eaten
        self.budget -= grass * 2 + meat * 4

    def dead_animals(self):
        for animal in self.animals:
            if animal.die() is True:
                self.animals.remove(animal)

    def gender_baby(self):
        random_number = random.random()
        if random_number > 0.5:
            return "male"
        return "female"

    def reproduce(self, animal1, animal2):
        if animal1.species == animal2.species and animal1.gender != animal2.gender:
            if animal1.gender == "female" and animal1.age - animal1.last_pregnancy >= 6:
                animal1.last_pregnancy = animal1.age
            elif animal2.age - animal2.last_pregnancy >= 6:
                animal2.last_pregnancy = animal2.age
            baby = Animal(animal1.species, 0, None, self.gender_baby(), self.weight)
            return baby
        else:
            return "Cannot reproduce"

