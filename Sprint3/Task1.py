def outer(name):
    def inner(): print(f'Hello, {name}!')
    return inner


if __name__ == '__main__':
    tom = outer("tom")
    tom()