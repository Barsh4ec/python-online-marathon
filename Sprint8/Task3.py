import unittest
import math

def quadratic_equation(a, b, c):
    if a == b == c == 0:
        raise ValueError
    dis = b ** 2 - 4 * a * c
    sqrt_val = math.sqrt(abs(dis))
    if dis > 0:
        return ((-b + sqrt_val) / (2 * a), (-b - sqrt_val) / (2 * a))
    elif dis == 0:
        return -b / (2 * a)

class QuadraticEquationTest(unittest.TestCase):
    def test_discr_equals_zero(self):
        self.assertEqual(quadratic_equation(2, 4, 2), -1)

    def test_discr_greater_zero(self):
        self.assertEqual(quadratic_equation(4, -3, -1), (1.0, -0.25))

    def test_discr_less_zero(self):
        self.assertEqual(quadratic_equation(4, -3, 1), None)

    def test_all_values_zero(self):
        with self.assertRaises(ValueError) as ve:
            quadratic_equation(0, 0, 0)

if __name__ == '__main__':
    print(quadratic_equation(2, 1, -1))