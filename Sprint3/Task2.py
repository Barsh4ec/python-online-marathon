def create(text):
    return lambda txt: True if text == txt else False


if __name__ == '__main__':
    tom = create("pass_for_Tom")
    print(tom("pass_for_Tom"))
    print(tom("pass_for_tom"))