def divide(numerator, denominator):
    try:
        return f'Result is {numerator/denominator}'
    except ZeroDivisionError:
        return f'Oops, {numerator}/{denominator}, division by zero is error!!!'
    except TypeError:
        return 'Value Error! You did not enter a number!'



if __name__ == '__main__':
    print(divide(8, 16))  # output:   "Result is 0.5"
    print(divide(5, 0))  # output:   "Oops, 5 / 0 denominator, division by zero is error!!!"
    print(divide("25", 5))  # output:   "Value Error! You did not enter a number!"
    print(divide("abc", 9))  # output:    "Value Error! You did not enter a number!"