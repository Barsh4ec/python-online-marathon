import json
import re
import uuid

class PasswordValidationException(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return self.data

class ForbiddenException(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return self.data

class NonUniqueException(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return self.data


def get_subjects_from_json(subjects):
    with open(subjects) as f:
        jsn = f.read()
    text = json.loads(jsn)
    result = []
    for item in text:
        result.append(Subject(item['title'], item['id']))
    return result


class User:
    def __init__(self, username, password, role, id=None, subject=None):
        self.username = username
        self.password = password
        self.role = role
        self.id = uuid.uuid4()
        self.subject = subject

    def __str__(self):
        if self.subject is None:
            return f'{self.username} with role {self.role}: []'
        else:
            return f'{self.username} with role {self.role}: {self.subject}'

    @staticmethod
    def create_user(username, password, role):
        regex = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{6,}$"
        if not re.search(regex, password):
            raise PasswordValidationException('data')
        return User(username, password, role)


    def add_score_for_subject(self, subject, score):
        if self.subject is None:
            self.subject = []
        self.subject.append({subject.name: score})

    def get_user_grades(self, user):
        return user.subject


def get_users_with_grades(users, subjects, grades):
    with open(users) as f:
        jsn = f.read()
    text = json.loads(jsn)

    result = []
    for item in text:
        with open(subjects) as f:
            jsn = f.read()
        subj = json.loads(jsn)
        with open(grades) as f:
            jsn = f.read()
        grades = json.loads(jsn)
        list_of_subjects = []
        for j in grades:
            for i in subj:
                if j['subject_id'] == i['id'] and item['id'] == j['user_id']:
                    list_of_subjects.append({i['title']: j['score']})
        result.append(User(item['username'], item['password'], item['role'], item['id'], list_of_subjects))
    return result


def get_grades_for_user(username, user, users):
    if user.role == 'Role.Mentor':
        for us in users:
            if us.username == username:
                if user.get_user_grades(us) is None:
                    return []
                else:
                    return user.get_user_grades(us)
    else:
        if user.username != username:
            raise ForbiddenException('data')
        for usr in users:
            if usr.username == username:
                if usr.subject is None:
                    return []
                else:
                    return usr.subject


class Subject:
    def __init__(self, name, id=None):
        self.name = name
        self.id = uuid.uuid4()


class Role:
    Mentor = 'Role.Mentor'
    Trainee = 'Role.Trainee'


class Score:
    B = 'B'
    D = 'D'


def add_user(user, users):
    for i in users:
        if i.username == user.username:
            raise NonUniqueException(f"User with name {user.username} already exists")
    users.append(user)
    result = users
    return result

def add_subject(subject, subjects):
    subjects.append(Subject(subject.name, subject.id))
    return subjects


def check_if_user_present(username, password, list):
    for item in list:
        if item.username == username and item.password == password:
            return True
    return False

def users_to_json(users, json_file):
    result = []
    for user in users:
        result.append({'username': user.username,
                       'role': user.role,
                       'subject': user.subject,
                       'password': user.password,
                       'id': str(user.id)[:20]})
    with open(json_file, 'w') as w:
        w.write(json.dumps(result, indent=4))

def subjects_to_json(subjects, json_file):
    result = []
    for subject in subjects:
        result.append({'name': subject.name,
                       'id': str(subject.id)[:20]})
    with open(json_file, 'w') as w:
        w.write(json.dumps(result, indent=4))

def grades_to_json(users, subjects, json_file):
    result = []
    for user in users:
        result.append({'username': user.username,
                       'role': user.role,
                       'subject': user.subject,
                       'password': user.password,
                       'user_id': str(user.id)[:20]})
    for subject in subjects:
        result.append({'name': subject.name,
                       'subject_id': str(subject.id)[:20]})
    with open(json_file, 'w') as w:
        w.write(json.dumps(result, indent=4))


def file_contains(json_file, key, value):
    with open(json_file, 'r') as r:
        jsn = r.read()
    data = json.loads(jsn)
    for item in data:
        try:
            if len(item[key]) == value:
                return True
        except KeyError:
            pass
    return False

if __name__ == '__main__':
    users = get_users_with_grades("users.json", "subjects.json", "grades.json")
    subjects = get_subjects_from_json("subjects.json")
    mentor = User.create_user("Mentor", "!1qQ456", Role.Mentor)
    add_user(mentor, users)
    user2 = User.create_user("Second", "Password_0", Role.Trainee)
    add_user(user2, users)
    user2.add_score_for_subject(subjects[1], Score.B)
    subject = Subject("New Subject")
    add_subject(subject, subjects)
    users[0].add_score_for_subject(subject, Score.D)

    grades_to_json(users, subjects, "987.json")
    print(file_contains("987.json", "user_id", 20))
    print(file_contains("987.json", "subject_id", 20))
