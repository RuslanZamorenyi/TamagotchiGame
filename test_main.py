import unittest
from main import Animal, add_data


class TestCalculator(unittest.TestCase):
    def test_init_func(self):
        try:
            animal2 = Animal(-15, 70, 70, 70, 70)
        except:
            result2 = "object not created"
        try:
            animal3 = Animal(55, 70, 70, 70)
        except:
            result3 = "object not created"
        try:
            animal4 = Animal(20, 70, 70, 70, 70, "hello")
        except:
            result4 = "object not created"
        self.assertEqual(result2, "object not created")
        self.assertEqual(result3, "object not created")
        self.assertEqual(result4, "object not created")

    def test_level_food(self):
        animal = Animal(55, 80, 60, 70, 10)
        animal1 = Animal(55, 80, 60, 70, 10)
        result = animal.level_food()
        result1 = animal1.time_work()
        print(result1)
        self.assertEqual(result1, "f")
        self.assertEqual(result, (65, 10))

    def test_level_water(self):
        animal = Animal(5, 10, 40, 20, 50)
        result = animal.level_water()
        self.assertEqual(result, (20, 50))

    def test_level_entertainment(self):
        animal = Animal(5, 10, 50, 20, 30)
        result = animal.level_entertainment()
        self.assertEqual(result, (60, 30))

    def test_level_sleep(self):
        animal = Animal(55, 90, 35, 10, 20)
        result = animal.level_sleep()
        self.assertEqual(result, (20, 20))


if __name__ == '__main__':
    unittest.main()
