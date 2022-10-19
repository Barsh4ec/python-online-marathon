import random

def randomWord(args):
    if not args:
        yield None
    while True:
        copy_args = args.copy()
        while len(copy_args) > 0:
            rand = random.randrange(0, len(copy_args))
            word = copy_args[rand]
            copy_args.pop(rand)
            yield word

if __name__ == '__main__':
    words = [3, 4, 7]
    rand = randomWord([3, 2, 90])
    list1 = []
    list2 = []
    for i in range(len(words)):
        list1.append(next(rand))
    for i in range(len(words)):
        list2.append(next(rand))
    print(list1 != list2)