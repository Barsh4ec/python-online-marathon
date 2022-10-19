class MyError(Exception):
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return self.data


def check_positive(number):
    try:
        if float(number) >= 0:
            return f'You input positive number: {float(number)}'
        else:
            return MyError(f'You input negative number: {float(number)}. Try again.')
    except MyError as r:
        return r.data
    except ValueError:
        return 'Error type: ValueError!'


if __name__ == '__main__':
    print(check_positive(24))  # output:    "You input positive number: 24"
    print(check_positive(-19))  # output:     "You input negative number: -19. Try again."
    print(check_positive("38"))  # output:    "You input positive number: 38"
    print(check_positive("abc"))  # output:     "Error type: ValueError!"