def toPostFixExpression(e):
    brackets = ['(', ')']
    operators = ['-', '+', '*', '/', '%']
    list_of_operators = []
    result = []
    for item in e:
        if item not in operators and item not in brackets:
            result.append(item)
        if item in operators:
            list_of_operators.append(item)
        if item == ')':
            result.extend(list_of_operators[::-1])
            list_of_operators.clear()
    result.extend(list_of_operators[::-1])
    return result


if __name__ == '__main__':
    a = ["20", "+", "3", "*", "(", "5", "*", "4", ")"]
    print(toPostFixExpression(a))