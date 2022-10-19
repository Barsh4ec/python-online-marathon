def morse_number(input):
    result = ''
    for item in input:
        tmp = ''
        if int(item) <= 5:
            while len(tmp) < int(item):
                tmp += '.'
            while len(tmp) < 5:
                tmp += '-'
        if int(item) > 5:
            while len(tmp) < 10 - int(item):
                 tmp += '.'
            while len(tmp) < 5:
                tmp += '-'
            tmp = tmp[::-1]
        result += tmp + ' '
    return result[:-1]



if __name__ == '__main__':
    print(morse_number("295"))