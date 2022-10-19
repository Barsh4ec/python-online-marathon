def divisor(num):
    for i in range(1, num + 1):
        if num % i == 0:
            yield i
    yield None
    yield None


if __name__ == '__main__':
    func = divisor(10)
    print(next(func))
    print(next(func))
    print(next(func))
    print(next(func))
    print(next(func))
    print(next(func))
    print(next(func))
    print(next(func))
