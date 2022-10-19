def logger(func):
    def wrapper(*args, **kwargs):
        lst_to_str = ', '.join(str(item) for item in list(args) + list(kwargs.values()))
        result = func(*args, **kwargs)
        print(f'Executing of function {func.__name__} with arguments {lst_to_str}...')
        return result
    return wrapper

@logger
def concat(*args, **kwargs):
    return ''.join(str(item) for item in list(args) + list(kwargs.values()))


if __name__ == '__main__':
    print(concat('first string', second=2, third='second string'))