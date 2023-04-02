import unittest
from main import Animal


class TestCalculator(unittest.TestCase):

    def test_start_play(self):
        animal = Animal(70, 70, 70, 70, 70)
        result = animal.start_play()
        self.assertEqual(result, )


    def test_level_food(self):

        animal = Animal(70, 70, 70, 70, 70)
        result = animal.start_play().level_food()
        self.assertEqual(result, )


if __name__ == '__main__':
    unittest.main()
