import json
from json import JSONEncoder


class Student:
    def __init__(self, full_name, avg_rank, courses):
        self.full_name = full_name
        self.avg_rank = avg_rank
        self.courses = courses

    def __str__(self):
        return f'{self.full_name} ({self.avg_rank}): {self.courses}'

    def __repr__(self):
        return repr(self.__str__())

    @staticmethod
    def from_json(file):
        with open(file) as f:
            jsn = f.read()
        student = json.loads(jsn)
        return Student(student["full_name"], student["avg_rank"], student["courses"])

    @classmethod
    def serialize_to_json(cls, user, file):
        result = {"full_name": user.full_name,
                  "avg_rank": user.avg_rank,
                  "courses": user.courses}
        with open(file, 'w') as w:
            json.dump(result, w)

class Group:
    def __init__(self, title, students):
        self.title = title
        self.students = students

    def __str__(self):
        res = []
        for item in self.students:
            res.append(f"{item['full_name']} ({item['avg_rank']}): {item['courses']}")
        return f'{self.title}: {res}'

    @classmethod
    def create_group_from_file(cls, file):
        with open(file) as f:
            jsn = f.read()
        group = json.loads(jsn)
        if isinstance(group, list):
            return Group(file.title()[:-5], [item for item in group])
        else:
            return Group(file.title()[:-5], [group])

    @classmethod
    def serialize_to_json(cls, list_of_groups, filename):
        result = []
        for item in list_of_groups:
            result.append({
                "title": item.title,
                "students": item.students
            })
        with open(filename, 'w') as w:
            json.dump(result, w)


if __name__ == '__main__':
    user1 = Student.from_json("2020-01.json")
    Student.serialize_to_json(user1, "test_student.json")

    g1 = Group.create_group_from_file("2020_2.json")
    print(g1)
    g2 = Group.create_group_from_file("2020-01.json")
    print(g2)
    Group.serialize_to_json([g1, g2], "g1")