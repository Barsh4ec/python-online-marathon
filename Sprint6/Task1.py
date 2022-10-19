import json

def find(file, key):
    with open(file) as f:
        jsn = f.read()
    result = []
    print(jsn)
    def as_key(dct):
        if key in dct:
            if isinstance(dct[key], list):
                result.extend(dct[key])
            else:
                result.append(dct[key])
    json.loads(jsn, object_hook=as_key)
    return list(set(result))


if __name__ == '__main__':
    path = 'example.json'
    print(find(path, 'password'))