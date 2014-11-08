from zoo import Zoo
from animal import Animal
import json


class ZooGarden:

    def __init__(self):
        self.zoo = Zoo(50, 10000)

    def see_animals(self):
        if len(self.zoo.animals) != 0:
            for animal in self.zoo.animals:
                print(animal)
        else:
            print("\nThere are no animals yet. Accomodate some?")

    def accomodate(self, species, name, age, weight):
        gender = input("What gender is the animal?: ")
        self.zoo.accommodate(species, age, name, gender, weight)

    def move_to_habitat(self, species, name):
        has_such_animal = False
        for animal in self.zoo.animals:
            if animal.species == species and animal.name == name:
                print("{} is now a free {}!".format(animal.name,
                                                    animal.species))
                self.zoo.animals.remove(animal)
                Animal.SPECIES_NAMES[animal.species].remove(animal.name)
                has_such_animal = True
        if not has_such_animal:
            print("\nThere is no such animal in the zoo anyway.")

    def simulate(self, interval_of_time, period):
        if len(self.zoo.animals) != 0:
            time_in_months = self.__time_in_months(interval_of_time, period)

            for female in self.zoo.animals:
                for male in self.zoo.animals:
                    self.zoo.reproduce(female, male)

            self.__grow_all_animals(time_in_months)
            print('\nTheese animals have grown:')
            self.see_animals()

            self.__print_dead_animals(self.zoo.dead_animals())

            self.__could_budget_afford_food(time_in_months)

            self.__born_animals()
        else:
            print("\nThere are no animals yet. Accomodate some?")

    def __time_in_months(self, interval_of_time, period):
        if interval_of_time == 'days':
            return period * 1 / 30  # rough approximation
        elif interval_of_time == 'weeks':
            return period * 1 / 4  # rough approximation
        elif interval_of_time == 'months':
            return period
        elif interval_of_time == 'years':
            return period * 12
        else:
            print("\nWrong interval of time, it should be "
                  "days, weeks, months or years.")

    def __grow_all_animals(self, time_in_months):
        for animal in self.zoo.animals:
            animal.grow(time_in_months)

    def __print_dead_animals(self, list_dead_animals):
        if len(list_dead_animals) != 0:
            print("\nTheese animals had died:")
            for animal in list_dead_animals:
                print(animal)
        else:
            print("\nNo animals have died.")

    def __could_budget_afford_food(self, time_in_months):
        time_in_days = time_in_months * 30  # rough approximation
        self.zoo.budget += self.zoo.get_income() * time_in_days

        self.zoo.get_outcome()

        if self.zoo.budget >= 0:
            print("\nZoo's budget can afford feeding all animals:)")
        else:
            print("T\nhere aren't enough money to feed all animals."
                  "Move some to habitat?")

    def __born_animals(self):
        babies = self.zoo.newborn_baby()
        if len(babies) != 0:
            print("\nZoo's babies are:")
            for baby in babies:
                print(baby)
        else:
            print("\nThere're no babies.")

    def show_database_species(self):
        file = open("database.json", "r")
        content = json.loads(file.read())
        file.close()
        print("\nDatabase species are:")
        for species_key in content:
            print(species_key)

    def interface(self):

        print("\nWelcome to our Zoo! You can use one of the following"
              " commands:"
              "\n\nshow_database_species -> to know wich species"
              " are in our database"
              "\n\nsee_animals -> to see all current animals"
              "\n\naccomodate <species> <name> <age_in_months> <weight_in_"
              "kilos> -> to add animal in the zoo"
              "\n\nmove_to_habitat <species> <name> -> removes an animal from "
              "the Zoo and returns it to its natural habitat"
              "\n\nsimulate <interval_of_time> <period> -> shows what happens"
              " in the Zoo for that time"
              "\n - <interval_of_time> is 'days', 'weeks', 'months' or 'years'"
              "\n - <period> is a number"
              "\n\nexit -> to exit the program")

        while True:
            reply = input("\nYour choice: ")
            if reply == 'exit':
                break
            else:
                reply = reply.split()  # make list of arguments
                if reply[0] == "see_animals":
                    self.see_animals()
                elif reply[0] == "accomodate" and len(reply) == 5:
                    self.accomodate(reply[1], reply[2],
                                    float(reply[3]), float(reply[4]))
                elif reply[0] == "move_to_habitat" and len(reply) == 3:
                    self.move_to_habitat(reply[1], reply[2])
                elif reply[0] == "simulate" and len(reply) == 3:
                    self.simulate(reply[1], float(reply[2]))
                elif reply[0] == "show_database_species":
                    self.show_database_species()
                else:
                    print("Wrong command! Try again.")


def main():
    ZooGarden().interface()

if __name__ == '__main__':
    main()
