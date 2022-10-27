import unittest

class Product:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count


class Cart:
    def __init__(self, products):
        self.products = products

    def get_total_price(self):
        price = 0
        for item in self.products:
            if 0 <= item.count <= 4:
                price += item.price * item.count
            elif 5 <= item.count <= 6:
                price += (item.price * item.count / 100 * 95)
            elif 7 <= item.count <= 9:
                price += (item.price * item.count / 100 * 90)
            elif 10 <= item.count <= 19:
                price += (item.price * item.count / 100 * 80)
            elif item.count == 20:
                price += (item.price * item.count / 100 * 70)
            elif item.count > 20:
                price += (item.price * item.count / 100 * 50)
        return price


class CartTest(unittest.TestCase):
    def test_is_equal(self):
        products = (Product('p1', 10, 4),
                    Product('p2', 100, 5),
                    Product('p3', 200, 6),
                    Product('p4', 300, 7),
                    Product('p5', 400, 9),
                    Product('p6', 500, 10),
                    Product('p7', 1000, 20))
        cart = Cart(products)
        self.assertEqual(cart.get_total_price(), 24785.0)



if __name__ == '__main__':
    products = (Product('p1', 10, 4),
                Product('p2', 100, 5),
                Product('p3', 200, 6),
                Product('p4', 300, 7),
                Product('p5', 400, 9),
                Product('p6', 500, 10),
                Product('p7', 1000, 20))
    cart = Cart(products)
    print(cart.get_total_price())