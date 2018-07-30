import unittest
from my_library import power_two, mult_nums

class TestMyCase(unittest.TestCase):

    def test_first_test(self):

        self.assertEqual(1, 1)

    def test_power_two(self):

        self.assertEqual(power_two(2), 4)
        self.assertEqual(power_two(5), 25)
        self.assertEqual(power_two(-15), 225)

    def test_mult_nums(self):

        self.assertEqual(mult_nums(1,2), 2)
        self.assertEqual(mult_nums(14, 2), 28)
        self.assertEqual(mult_nums(111, -12), -1332)

    def test_integration(self):
        self.assertEqual(power_two(3), mult_nums(3, 3))

unittest.main()