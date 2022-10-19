def kthTerm(n, k):
    result = [0]
    for j in range(0, n):
        count = 0
        for i in range(len(result)):
            result.append((n ** j) + result[count])
            count += 1
        if len(result) > k:
            print(result)
            break
    return k if len(result) < k else result[k]


if __name__ == '__main__':
    n = int(input('n = '))
    k = int(input('k = '))
    print(kthTerm(n, k))