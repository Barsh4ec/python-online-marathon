from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def cook(self):
        pass


class FettuccineAlfredo(Product):
    def cook(self):
        print('Italian main course prepared: Fettuccine Alfredo')


class Tiramisu(Product):
    def cook(self):
        print('Italian dessert prepared: Tiramisu')


class DuckALOrange(Product):
    def cook(self):
        print("French main course prepared: Duck À L'Orange")


class CremeBrulee(Product):
    def cook(self):
        print('French dessert prepared: Crème brûlée')


class Factory(ABC):
    @abstractmethod
    def get_dish(self, type_of_meal):
        pass


class ItalianDishesFactory(Factory):
    def get_dish(self, type_of_meal):
        return FettuccineAlfredo() if type_of_meal == 'main' else Tiramisu()


class FrenchDishesFactory(Factory):
    def get_dish(self, type_of_meal):
        return DuckALOrange() if type_of_meal == 'main' else CremeBrulee()


class FactoryProducer:
    def get_factory(self, type_of_factory):
        return ItalianDishesFactory() if type_of_factory == 'italian' else FrenchDishesFactory()


if __name__ == '__main__':
    fp = FactoryProducer()
    fac = fp.get_factory("italian")
    main_dish = fac.get_dish("main")
    main_dish.cook()