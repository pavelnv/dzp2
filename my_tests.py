import unittest
from my_library import power_two

class TestMyCase(unittest.TestCase):

    def test_first_test(self):

        self.assertEqual(1, 1)

    def test_power_two(self):

        self.assertEqual(power_two(2), 4)
        self.assertEqual(power_two(5), 25)
        self.assertEqual(power_two(-15), 225)



unittest.main()