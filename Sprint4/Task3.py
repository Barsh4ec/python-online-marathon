class Employee:
    def __init__(self, fullname, **kwargs):
        splited = fullname.split(' ')
        self.name = splited[0]
        self.lastname = splited[1]
        for key in kwargs:
            setattr(Employee, key, kwargs[key])


if __name__ == '__main__':
    john = Employee("John Doe")
    mary = Employee("Mary Major", salary=120000)
    richard = Employee("Richard Roe", salary=110000, height=178)
    giancarlo = Employee("Giancarlo Rossi", salary=115000, height=182, nationality="Italian")
    print(mary.lastname)# ➞ "Major"
    print(richard.height)# ➞ 178
    print(giancarlo.nationality)# ➞ "Italian"
    print(john.name)# ➞ "John"