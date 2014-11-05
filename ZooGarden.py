from zoo import Zoo
from animal import Animal


class ZooGarden:

    def __init__(self):
        self.zoo = Zoo(50, 10000)

    def see_animals(self):
        if len(self.zoo.animals) != 0:
            for animal in self.zoo.animals:
                print(animal)
        else:
            print("There are no animals yet. Accomodate some?")

    def accomodate(self, species, name, age, weight):
        gender = input("What gender is the animal?: ")
        self.zoo.accommodate(species, age, name, gender, weight)

    def move_to_habitat(self, species, name):
        for animal in self.zoo.animals:
            if animal.species == species and animal.name == name:
                self.zoo.animals.remove(animal)
                Animal.SPECIES_NAMES[animal.species].remove(animal.name)

    def simulate(self, interval_of_time, period):
        if len(self.zoo.animals) != 0:
            time_in_months = self.time_in_months(interval_of_time, period)
            self.grow_all_animals(time_in_months)
            self.see_animals()

            self.print_dead_animals(self.zoo.dead_animals())

            self.could_budget_afford_food(time_in_months)

            self.born_animals()
        else:
            print("There are no animals yet. Accomodate some?")

    def time_in_months(self, interval_of_time, period):
        if interval_of_time == 'days':
            return period * 1 / 30  # rough approximation
        elif interval_of_time == 'weeks':
            return period * 1 / 4  # rough approximation
        elif interval_of_time == 'months':
            return period
        elif interval_of_time == 'years':
            return period * 12
        else:
            print("Wrong interval of time, it should be "
                  "days, weeks, months or years.")

    def grow_all_animals(self, time_in_months):
        for animal in self.zoo.animals:
            animal.grow(time_in_months)

    def print_dead_animals(self, list_dead_animals):
        if len(list_dead_animals) != 0:
            for animal in list_dead_animals:
                print(animal)
        else:
            print("No animals have died.")

    def could_budget_afford_food(self, time_in_months):
        self.zoo.budget += self.zoo.get_income() * time_in_months * 30

        self.zoo.get_outcome()

        if self.zoo.budget >= 0:
            print("Zoo's budget can afford feeding all animals:)")
        else:
            print("There aren't enough money to feed all animals."
                  "Move some to habitat?")

    def born_animals(self, time_in_months):

        # need discussion:)
        pass

    def interface(self):

        print("\nWelcome to our Zoo! You can use one of the following"
              " commands:"
              "\nsee_animals -> to see all current animals"
              "\naccomodate <species> <name> <age> <weight> ->"
              " to add animal in the zoo"
              "\nmove_to_habitat <species> <name> -> removes an animal from "
              "the Zoo and returns it to its natural habitat"
              "\nsimulate <interval_of_time> <period> -> shows what happens"
              " in the Zoo for that time"
              "\n - <interval_of_time> is 'days', 'weeks', 'months' or 'years'"
              "\n - <period> is a number"
              "\nexit -> to exit the program")

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
                else:
                    print("Wrong command! Try again.")


def main():
    ZooGarden().interface()

if __name__ == '__main__':
    main()
