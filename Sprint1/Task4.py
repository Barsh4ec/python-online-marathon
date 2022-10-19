def findPermutation(p, q):
    return ([p.index(item) + 1 for item in q])


if __name__ == '__main__':
    p = [3, 4, 1, 2, 5]
    q = [4, 5, 2, 3, 1]
    print(findPermutation(p, q)) #25413