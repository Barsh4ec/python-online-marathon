def double_string(data):
    counter = 0
    mas = []
    for item1 in data:
        for item2 in data:
            if item1+item2 not in mas:
                counter += data.count(item1+item2)
                mas.append(item1+item2)
    return counter


if __name__ == '__main__':
    data = ['aa', 'aaaa', 'aaaaaaaa', 'aaaa', 'qwer', 'qwerqwert']
    print(double_string(data))