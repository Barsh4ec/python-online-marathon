class Washing:
    def __init__(self):
        pass

    def wash(self):
        return 'Washing...'

class Rinsing:
    def __init__(self):
        pass

    def rinse(self):
        return 'Rinsing...'


class Spinning:
    def __init__(self):
        pass

    def spin(self):
        return 'Spinning...'

class WashingMachine:
    def __init__(self):
        self.sub_system_clas_washing = Washing()
        self.sub_system_clas_rinsing = Rinsing()
        self.sub_system_clas_spinning = Spinning()
        self.startWashing()

    def startWashing(self):
        print(self.sub_system_clas_washing.wash())
        print(self.sub_system_clas_rinsing.rinse())
        print(self.sub_system_clas_spinning.spin())

if __name__ == '__main__':
    washingMachine = WashingMachine()
    washingMachine.startWashing()