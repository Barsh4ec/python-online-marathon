import re

def pretty_message(text):
    text = re.compile(r'(...)\1*').sub(r'\1', text)
    text = re.compile(r'(\w\w)\1*').sub(r'\1', text)
    text = re.compile(r'(\w)\1*').sub(r'\1', text)
    return text


if __name__ == '__main__':
    data = "Thisssssssss isisisis echooooooo stringggg. Replaceaceaceace repeatedededed groupssss of symbolssss"
    print(pretty_message(data))