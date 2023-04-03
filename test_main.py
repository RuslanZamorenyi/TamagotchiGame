import unittest
from main import Animal


class TestCalculator(unittest.TestCase):
    def test_start_play(self):
        animal = Animal(70, 70, 70, 70, 70)
        result = animal.start_play()
        print(result)
        self.assertEqual(result, 'exit')

    def test_level_food(self):
        animal = Animal(70, 70, 70, 70, 70)
        result = animal.level_food()
        self.assertEqual(result, (80, 70))

    def test_level_water(self):
        animal = Animal(70, 80, 70, 70, 50)
        result = animal.level_water()
        self.assertEqual(result, (90, 50))

    def test_level_entertainment(self):
        animal = Animal(70, 70, 20, 70, 70)
        result = animal.level_entertainment()
        self.assertEqual(result, (30, 70))

    def test_level_sleep(self):
        animal = Animal(70, 70, 70, 100, 70)
        result = animal.level_sleep()
        self.assertEqual(result, (110, 40))




if __name__ == '__main__':
    unittest.main()
