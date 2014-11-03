import unittest
from animal import Animal
import json


class AnimalTests(unittest.TestCase):

#  дава грешка, понеже за всеки тест създава такава чайка, а името е вече заето
#  т.е. всеки тест трябва да си прави лично животно животно?
#    def setUp(self):
#        self.animal = Animal("seagull", 3, "Poll", 'male', 1.250)

    def test__init(self):
        self.animal = Animal("seagull", 3, "Poll 1", 'male', 1.250)
        self.assertEqual("seagull", self.animal.species)
        self.assertEqual(3, self.animal.age)
        self.assertEqual("Poll 1", self.animal.name)
        self.assertEqual('male', self.animal.gender)
        self.assertEqual(1.250, self.animal.weight)
        self.assertEqual({"seagull": ["Poll 1"]}, self.animal.SPECIES_NAMES)

    def test_set_name(self):
        self.animal = Animal("seagull", 3, "Poll 2", 'male', 1.250)
        self.assertEqual("Mark", self.animal.set_name("Mark"))

    def test_set_name_already_exists_value_error(self):
        with self.assertRaises(ValueError):
            Animal("seagull", 3, "Poll 1", "male", 1.250)

    def test_grow(self):
        self.animal = Animal("seagull", 3, "Poll 3", 'male', 1.250)
        self.animal.grow()
        self.assertEqual(1.750, self.animal.weight)
        self.assertEqual(4, self.animal.age)

    def test_eat(self):
        self.animal = Animal("seagull", 3, "Poll 4", 'male', 1.250)
        self.assertTrue(self.animal.eat())

    def test_die(self):
        self.animal = Animal("seagull", 3, "Poll 5", 'male', 1.250)
        file = open("database.json", "r")
        content = file.read()
        file.close()
        # in database.json the age is in days, while self.age is in years
        life_expectancy = json.loads(content)["life_expectancy"] // 356

        self.animal.age = 0
        self.assertFalse(self.animal.die())

        self.animal.age = life_expectancy
        self.assertTrue(self.animal.die())

if __name__ == '__main__':
    unittest.main()
