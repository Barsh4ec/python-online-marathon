import unittest

class Worker:
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary
        if self.salary < 0:
            raise ValueError

    def get_tax_value(self):
        limit_1, limit_2, limit_3, limit_4, limit_5, limit_6 = 1000, 3000, 5000, 10000, 20000, 50000
        rate_1, rate_2, rate_3, rate_4, rate_5, rate_6, rate_7 = 0, 0.10, 0.15, 0.21, 0.30, 0.40, 0.47

        if self.salary < limit_1:
            tax = 0.0
        elif self.salary < limit_2:
            tax = rate_1 * limit_1 + rate_2 * (self.salary - limit_1)
        elif self.salary < limit_3:
            tax = rate_1 *\
                  limit_1 + rate_2 * (limit_2 - limit_1) + \
                  rate_3 * (self.salary - limit_2)
        elif self.salary < limit_4:
            tax = rate_1 * limit_1 + \
                  rate_2 * (limit_2 - limit_1) + \
                  rate_3 * (limit_3 - limit_2) + \
                  rate_4 * (self.salary - limit_3)
        elif self.salary < limit_5:
            tax = rate_1 * limit_1 + \
                  rate_2 * (limit_2 - limit_1) + \
                  rate_3 * (limit_3 - limit_2) + \
                  rate_4 * (limit_4 - limit_3) + \
                  rate_5 * (self.salary - limit_4)
        elif self.salary < limit_6:
            tax = rate_1 * limit_1 + \
                  rate_2 * (limit_2 - limit_1) + \
                  rate_3 * (limit_3 - limit_2) + \
                  rate_4 * (limit_4 - limit_3) + \
                  rate_5 * (limit_5 - limit_4) + \
                  rate_6 * (self.salary - limit_5)
        else:
            tax = rate_1 * limit_1 + \
                  rate_2 * (limit_2 - limit_1) + \
                  rate_3 * (limit_3 - limit_2) + \
                  rate_4 * (limit_4 - limit_3) + \
                  rate_5 * (limit_5 - limit_4) + \
                  rate_6 * (limit_6 - limit_5) + \
                  rate_7 * (self.salary - limit_6)
        return tax

class WorkerTest(unittest.TestCase):
    def setUp(self):
        self.name = 'Vika'
        self.value = -4

    @unittest.expectedFailure
    def test_negative_values(self):
        Worker(self.name, self.value)
        self.had_exception = False

    def test_valid_values(self):
        worker = Worker(self.name, 100000)
        self.assertEqual(worker.get_tax_value(), 40050.0)

    def tearDown(self):
        self.name = None
        self.value = None

if __name__ == '__main__':
    worker = Worker("Vika", 100000)
    print(worker.get_tax_value())