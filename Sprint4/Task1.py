class Employee:
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    @staticmethod
    def from_string(string):
        arg = string.split('-')
        return Employee(arg[0], arg[1], int(arg[2]))


if __name__ == '__main__':
    emp1 = Employee("Mary", "Sue", 60000)
    emp2 = Employee.from_string("John-Smith-55000")
    print(emp1.firstname)# ➞ "Mary"
    print(emp1.salary)# ➞ 60000
    print(emp2.firstname)# ➞ "John"