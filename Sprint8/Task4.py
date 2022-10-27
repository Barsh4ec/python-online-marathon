import unittest
import math

class TriangleNotValidArgumentException(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return self.data


class TriangleNotExistException(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return self.data


class Triangle:
    def __init__(self, data):
        if isinstance(data, tuple) and len(data) == 3:
            for item in data:
                if not isinstance(item, int):
                    raise TriangleNotValidArgumentException("Not valid arguments")
        else:
            raise TriangleNotValidArgumentException("Not valid arguments")
        self.a = data[0]
        self.b = data[1]
        self.c = data[2]
        if self.a >= self.b + self.c or self.b >= self.a + self.c or self.c >= self.b + self.a:
            raise TriangleNotExistException("Can`t create triangle with this arguments")

    def get_area(self):
        return 1 / 4 * math.sqrt((self.a + self.b + self.c) * (self.b + self.c - self.a) *
                                 (self.a + self.c - self.b) * (self.a + self.b - self.c))


class TriangleTest(unittest.TestCase):
    def test_valid_values(self):
        triangle = Triangle((120, 109, 13))
        self.assertEqual(triangle.get_area(), 396.0)

    def test_not_valid_sides(self):
        with self.assertRaises(TriangleNotExistException) as ve:
            Triangle((1100, 5, 1200))

    def test_not_valid_input(self):
        with self.assertRaises(TriangleNotValidArgumentException) as ve:
            Triangle(('text', 5))


if __name__ == '__main__':
    not_valid_arguments = [
        ('3', 4, 5),
        ('a', 2, 3),
        'string',
        (7, 2),
        (7, 7, 7, 7),
        10
    ]
    for data in not_valid_arguments:
        try:
            Triangle(data)
        except TriangleNotValidArgumentException as e:
            print(e)