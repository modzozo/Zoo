from animal import Animal
import random

class Zoo:
    ANIMAL_INCOME = 60
    MEAT_1KG_PRICE = 4
    GRASS_1KG_PRICE = 2

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
        self.budget += 60 * len(self.animals)

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
        list_dead_aniamals = []
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
        #TODO

    def newborn_baby(self):
        pass

    def reproduce(self):
        for animal in self.animals:
            if animal.gender="female" and animal1.gender != animal2.gender:
            if animal1.gender == "female" and animal1.age - animal1.last_pregnancy >= 6:
                animal1.last_pregnancy = animal1.age
            elif animal2.age - animal2.last_pregnancy >= 6:
                animal2.last_pregnancy = animal2.age
            baby = Animal(animal1.species, 0, animal1.set_name(), self.gender_baby(), None)
            self.animals.append(baby)
        else:
            message = "Cannot reproduce. Try again later"
            raise ValueError(message)

