class ToSmallNumberGroupError(Exception):
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return repr(self.data)


def check_number_group(number):
    try:
        if int(number) > 10:
            return f'Number of your group {number} is valid'
        else:
            raise ToSmallNumberGroupError("We obtain error:Number of your group can't be less than 10")
    except ToSmallNumberGroupError as e:
        return e.data
    except ValueError:
        return 'You entered incorrect data. Please try again.'

if __name__ == '__main__':
    print(check_number_group(4))   # output:    "We obtain error: Number of your group can't be less than 10 "
    print(check_number_group(59))  # output:    "Number of your group 59 is valid"
    print(check_number_group("25"))        # output:    "Number of your group 25 is valid"
    print(check_number_group("abc"))       # output:    "You entered incorrect data. Please try again."