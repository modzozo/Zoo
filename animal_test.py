import unittest
from animal import Animal


class AnimalTests(unittest.TestCase):

#  дава грешка, понеже за всеки тест създава такава чайка, а името е вече заето
#  т.е. всеки тест трябва да си прави лично животно?
#    def setUp(self):
#        self.animal = Animal("seagull", 3, "Stamat", 'male', 1.250)

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

    def test_set_weight_passed_argument(self):
        self.animal = Animal("bear", 14, "Poll 8", 'male', 10.0)
        self.assertEqual(42, self.animal._Animal__set_kilos_weight(42))

    def test_set_weight_no_passed_argument_take_newborn_weight(self):
        self.animal = Animal("bear", 14, "Poll 9", 'male', 2)
        self.assertEqual(self.animal.json_species_data['newborn_weight'],
                         self.animal._Animal__set_kilos_weight(None))

# __set_json_data_for_species which are in database is already tested

    def test_set_json_species_data_species_not_in_database(self):
        self.animal = Animal("bear", 14, "Poll 10", 'male', 10.0)
        self.assertEqual(None, self.animal._Animal__set_json_species_data(
            "database.json", "seagull"))

    def test_grow(self):
        self.animal = Animal("bear", 3, "Poll 11", 'male', 10.0)
        self.animal.grow(3)
        self.assertEqual(54, self.animal.kilos_weight)
        self.assertEqual(6, self.animal.age_in_months)
        # missing tests for pregnancy and the new functions
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    def test_grow_average_weight_reached(self):
        self.animal = Animal("bear", 3, "Poll 12", 'male', 10.0)
        self.animal.grow(10)
        self.assertEqual(100, self.animal.kilos_weight)

    def test_eat(self):
        self.animal = Animal("bear", 3, "Poll 13", 'male', 10.0)
        self.assertEqual(2, self.animal.eat())

    def test_die_still_alive(self):
        self.animal = Animal("bear", 3, "Poll 14", 'male', 10.0)

        self.animal.age = 0
        self.assertFalse(self.animal.die())

    def test_die_true(self):
        self.animal = Animal("bear", 3, "Poll 15", 'male', 10.0)

        self.animal.age = 1
        self.assertTrue(self.animal.die())
        self.assertTrue(self.animal.name not in Animal.SPECIES_NAMES)

    def test_str(self):
        self.animal = Animal("bear", 3, "Poll 16", 'male', 10.0)
        self.assertEqual("Poll 16: bear, 3 months, 10.0 kilos",
                         self.animal.__str__())

if __name__ == '__main__':
    unittest.main()
