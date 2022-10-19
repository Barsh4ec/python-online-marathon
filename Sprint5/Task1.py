import re

def valid_email(email):
    regex = r'^[\w\.]+@([a-zA-Z0-9]+\.)+[a-zA-Z0-9]{2,4}$'
    return 'Email is valid' if re.search(regex, email) else 'Email is not valid'


    print(valid_email('trafik@ukr.tel.com'))