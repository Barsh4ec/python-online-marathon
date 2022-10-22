class Goods:
    def __init__(self, price, discount_strategy=None):
        self.price = price
        self.discount_strategy = discount_strategy
        self.price_after_discount()

    def __str__(self):
        return self.price_after_discount()

    def price_after_discount(self):
        if self.discount_strategy == None:
            return f'Price: {self.price}, price after discount: {self.price}'
        else:
            return f'Price: {self.price}, price after discount: {self.discount_strategy(self.price)}'


def on_sale_discount(order):
    return order / 2


def twenty_percent_discount(order):
    order = order / 100 * 80
    return order


if __name__ == '__main__':
    print(Goods(20000))
    print(Goods(20000, discount_strategy = twenty_percent_discount))  # Price: 20000, price after discount: 16000.0
    print(Goods(20000, discount_strategy = on_sale_discount))  # Price: 20000, price after discount: 10000.0
