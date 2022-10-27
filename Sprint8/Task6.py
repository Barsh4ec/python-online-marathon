import unittest

def file_parser(file, find, replace=None):
    with open(file, 'r') as f:
        text = f.read()
    if replace == None:
        return f'Found {text.count(find)} strings'
    else:
        return text.replace(find, replace)

class ParserTest(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(file_parser('parser.txt', 'better'), 'Found 8 strings')

    def test_not_valid_input(self):
        with self.assertRaises(FileNotFoundError) as ve:
            file_parser('simple_text', 'better')

if __name__ == '__main__':
    print(file_parser('parser.txt', 'better'))