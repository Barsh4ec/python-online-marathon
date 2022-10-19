def check_odd_even(number):
    try:
        if number % 2 == 0:
            return 'Entered number is even'
        else:
            return 'Entered number is odd'
    except TypeError:
        return 'You entered not a number.'


if __name__ == '__main__':
    print(check_odd_even('trafik@ukr.tel.com'))