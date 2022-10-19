import json
import pickle
from enum import Enum


class SerializeManager(object):
    def __init__(self, file_name, method):
        self.filename = file_name
        self.fileType = method.value

    def __enter__(self):
        self.file_obj = open(self.filename, self.fileType)
        return self
    def __exit__(self, type, value, traceback):
        self.file_obj.close()


    def serialize(self, object):
            if self.fileType == 'wb':
                self.file_obj.write(pickle.dumps(object))
            else:
                self.file_obj.write(json.dumps(object))



class FileType(Enum):
    JSON = 'w'
    BYTE = 'wb'


def serialize(object, filename, fileType):
    print(fileType.value)
    with SerializeManager(filename, fileType) as manager:
        manager.serialize(object)


if __name__ == '__main__':
    data = {"prop1": "value1", "prop2": "value2"}
    with SerializeManager("test_4.json", FileType.JSON) as user:
        user.serialize(data)