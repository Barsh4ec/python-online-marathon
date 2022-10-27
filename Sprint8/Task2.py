import unittest

def divide(num_1, num_2):
    return float(num_1) / num_2

class DivideTest(unittest.TestCase):
    def test_is_equal(self):
        self.assertEqual(divide(8, 4), 2.0)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError) as cm:
            divide(8, 0)

    def test_not_numeric(self):
        with self.assertRaises(ValueError) as ve:
            divide('some_text', 4)