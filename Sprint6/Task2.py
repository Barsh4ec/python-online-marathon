import json
import logging

def parse_user(output_file, *input_files):
    result, names = [], []
    for item in input_files:
        try:
            with open(item) as f:
                jsn = f.read()
            text = json.loads(jsn)
        except FileNotFoundError:
            logging.error(f"File {item} doesn't exist")
        for user in text:
            print('username = ', user['name'])
            try:
                if user['name'] not in names: #[print(j['name']) for j in result]:
                    result.append(user)
                    names.append(user['name'])
                    print('added to result')
            except KeyError:
                continue
    with open(output_file, 'w') as w:
        json.dump(result, w, indent=4)



if __name__ == '__main__':
    output = 'Task2output.json'
    parse_user(output, 'user1.json', 'user2.json')
    with open('Task2output.json', 'r') as d:
        print(d.read())