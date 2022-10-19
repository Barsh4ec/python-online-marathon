import json
import jsonschema
from jsonschema import validate
import csv

class DepartmentName(Exception):
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return self.data


class InvalidInstanceError(Exception):
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return self.data


def validate_json(data, schema):
    try:
        validate(instance=data, schema=schema)
    except jsonschema.exceptions.ValidationError:
        name_of_schema = 'department' if len(schema['required']) == 2 else 'user'
        raise InvalidInstanceError(f'Error in {name_of_schema} schema')


def user_with_department(csv_file, user_json, department_json):
    with open(user_json) as uj:
        u_jsn = uj.read()
    users = json.loads(u_jsn)
    users_schema = {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "name": {"type": "string"},
            "department_id": {"type": "number"}
        },
        "required": ['id', 'name', 'department_id'],
    }
    with open(department_json) as dj:
        d_jsn = dj.read()
    departments = json.loads(d_jsn)
    departments_schema = {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "name": {"type": "string"},
        },
        "required": ['id', 'name'],
    }
    data = []
    for user in users:
        validate_json(user, users_schema)
        for department in departments:
            validate_json(department, departments_schema)
            if user['department_id'] == department['id']:
                data.append([user['name'], department['name']])
        if f'"id": {user["department_id"]}' not in d_jsn:
            raise DepartmentName(f"Department with id {user['department_id']} doesn't exists")

    with open(csv_file, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['name','department'])
        writer.writerows(data)


if __name__ == '__main__':
    try:
        user_with_department("user_department.csv", "user_without_dep.json", "department.json")
    except DepartmentName as e:
        print(str(e))
