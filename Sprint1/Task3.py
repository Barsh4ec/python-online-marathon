def isPalindrome1(str):
    return sum(str.count(c) % 2 for c in set(str)) < 2


def isPalindrome(str):
    if len(str) == 0 or len(str) == str.count(str[0]):
        return True
    count = 0
    for i in str:
        if str.count(i) % 2 != 0:
            count += 1
    return False if count > 1 else True



if __name__ == '__main__':
    str = input('str = ')
    print(isPalindrome1(str))
    print(isPalindrome(str))