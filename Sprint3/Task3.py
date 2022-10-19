import re


def create_account(user_name, password, secret_words):
    regex = r'(?=.*[0-9])(?=.*[!_@#$%^&*])(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z!@_#$%^&*]{6,}'
    if not re.search(regex, password):
        raise ValueError
    def check(check_pass, check_secr_words):
        if check_pass != password or len(secret_words) != len(check_secr_words):
            return False
        check = lambda lst1, lst2: [item for item in lst1 if item not in lst2]
        if len(check(secret_words, check_secr_words)) > 1:
            return False
        if len(check(check_secr_words, secret_words)) > 1:
            return False
        return True
    return check


if __name__ == '__main__':
    tom = create_account("Tom", "Qwerty1_", ["1", "word"])
    check1 = tom("Qwerty1_", ["1", "word"])
    print('check1 = ', check1)
    check2 = tom("Qwerty1_", ["word"])
    print('check2 = ', check2)
    check3 = tom("Qwerty1_", ["word", "2"])
    print('check3 = ', check3)
    check4 = tom("Qwerty1!", ["word", "12"])
    print('check4 = ', check4)
