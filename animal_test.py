import unittest
from animal import Animal


class AnimalTests(unittest.TestCase):

    def test__init(self):
        self.animal = Animal("bear", 14, "Poll 1", 'male', 10.0)
        self.assertEqual("bear", self.animal.species)
        self.assertEqual(14, self.animal.age_in_months)
        self.assertEqual("Poll 1", self.animal.name)
        self.assertEqual('male', self.animal.gender)
        self.assertEqual(10.0, self.animal.kilos_weight)
        self.assertEqual({"bear": ["Poll 1"]}, self.animal.SPECIES_NAMES)

        self.assertEqual({"life_expectancy": 12,
                          "food_type": "meat",
                          "gestation_period": 6,
                          "newborn_weight": 20,
                          "average_weight": 100,
                          "weight_age_ratio": 9,
                          "food_weight_ratio": 0.2},
                         self.animal.json_species_data)

# Трябва ли да тествам невалидни Animal обекти,
# ако тествам set методите за данните?

    def test_set_species(self):
        self.animal = Animal("bear", 14, "Poll 2", 'male', 10.0)
        self.assertEqual("bear", self.animal._Animal__set_species("bear"))

    def test_set_species_no_such_species_in_database_value_error(self):
        self.animal = Animal("bear", 14, "Poll 3", 'male', 10.0)
        self.animal.json_species_data = None
        with self.assertRaises(ValueError):
            self.animal._Animal__set_species("seagull")

    def test_set_name(self):
        self.animal = Animal("bear", 14, "Poll 4", 'male', 10.0)
        self.assertEqual("Mark", self.animal._Animal__set_name("Mark"))

    def test_set_name_already_exists_value_error(self):
        self.animal = Animal("bear", 14, "Poll 5", 'male', 10.0)
        with self.assertRaises(ValueError):
            self.animal._Animal__set_name("Poll 5")

    def test_set_gender(self):
        self.animal = Animal("bear", 14, "Poll 6", 'male', 10.0)
        self.assertEqual("female", self.animal._Animal__set_gender("female"))

    def test_set_gender_value_error(self):
        self.animal = Animal("bear", 14, "Poll 7", 'male', 10.0)
        with self.assertRaises(ValueError):
            self.animal._Animal__set_gender("tomato")

    def test_set_kilos_weight_passed_argument(self):
        self.animal = Animal("bear", 14, "Poll 8", 'male', 10.0)
        self.assertEqual(42, self.animal._Animal__set_kilos_weight(42))

    def test_set_kilos_weight_no_passed_argument_take_newborn_weight(self):
        self.animal = Animal("bear", 14, "Poll 9", 'male', 2)
        self.assertEqual(self.animal.json_species_data['newborn_weight'],
                         self.animal._Animal__set_kilos_weight(None))

    def test_set_json_species_data_species_not_in_database(self):
        self.animal = Animal("bear", 14, "Poll 10", 'male', 10.0)
        self.assertEqual(None, self.animal._Animal__set_json_species_data(
            "database.json", "seagull"))

    def test_grow(self):
        self.animal_male = Animal("bear", 3, "Poll 11", 'male', 10.0)
        self.animal_male.grow(3)
        self.assertEqual(54, self.animal_male.kilos_weight)
        self.assertEqual(6, self.animal_male.age_in_months)

    def test_weight_simulated_time_average_weight_reached(self):
        self.animal = Animal("bear", 3, "Poll 12", 'male', 10.0)
        self.animal.grow(10)
        self.assertEqual(100, self.animal.kilos_weight)

    def test_pregnancy_simulated_time_pregnant_female(self):
        self.animal_female = Animal("bear", 13, "Pollinka 1", 'female', 10.0)
        self.animal_female.pregnant_period = 4
        self.animal_female.non_pregnant_period = None
        self.animal_female.grow(3)
        self.assertEqual(6, self.animal_female.pregnant_period)
        self.assertEqual(None, self.animal_female.non_pregnant_period)

    def test_pregnancy_simulated_time_non_pregnant_female(self):
        self.animal_female = Animal("bear", 13, "Pollinka 2", 'female', 10.0)
        self.animal_female.non_pregnant_period = 7
        self.animal_female.grow(3)
        self.assertEqual(6, self.animal_female.non_pregnant_period)
        self.assertEqual(None, self.animal_female.pregnant_period)

    def test_eat(self):
        self.animal = Animal("bear", 3, "Poll 13", 'male', 10.0)
        self.assertEqual(2, self.animal.eat())

    def test_die(self):
        # I don't know how to test this function
        # because it interacts with the global dictionary of names in Animal
        # and that brings some limitations
        pass

    def test_set_name_for_the_baby(self):
        # also not sure how to test such things
        pass

    def test_str(self):
        self.animal = Animal("bear", 3, "Poll 16", 'male', 10.0)
        self.assertEqual("Poll 16: bear, 3 months, 10.0 kilos",
                         self.animal.__str__())

if __name__ == '__main__':
    unittest.main()
