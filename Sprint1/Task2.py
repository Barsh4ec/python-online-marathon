def filterBible(scripture, book, chapter):
    return [item for item in scripture if item[:2] == book and item[2:5] == chapter]


if __name__ == '__main__':
    book = input('book = ')
    chapter = input('chapter = ')
    scripture = ["01001001", "01001002", "01002001", "01002002", "01002003", "02001001", "02001002", "02001003"]
    print(filterBible(scripture, book, chapter))