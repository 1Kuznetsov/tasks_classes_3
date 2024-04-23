class Group:
    def __init__(self, id, members):
        self.id = id
        self.members = members
        self.schedule = []


class Lecturer:
    def __init__(self, id, name, courses):
        self.id = id
        self.name = name
        self.courses = courses
        self.availability = {}


class Course:
    def __init__(self, id, name, lecturer, timings, classroom, group):
        self.id = id
        self.name = name
        self.lecturer = lecturer
        self.timings = timings
        self.classroom = classroom
        self.group = group


class Schedule:
    def __init__(self, courses, timings):
        self.courses = courses
        self.timings = timings


def read_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        groups = {}
        lecturers = {}
        courses = {}
        for line in lines:
            data = line.strip().split(';')
            if data[0] == 'ГРУППА':
                groups[data[1]] = Group(data[1], data[2:])
            elif data[0] == 'ПРЕПОДАВАТЕЛЬ':
                lecturers[data[1]] = Lecturer(data[1], data[2], [])
            elif data[0] == 'КУРС':
                courses[data[1]] = Course(data[1], data[2], lecturers[data[3]], data[4], data[5], groups[data[6]])
                lecturers[data[3]].courses.append(courses[data[1]])
                groups[data[6]].schedule.append(courses[data[1]])
    return groups, lecturers, courses


def get_group_schedule(group_id):
    groups, lecturers, courses = read_from_file('data.txt')
    return groups[group_id].schedule


def print_schedule(schedule):
    for course in schedule:
        print(f"{course.name}: {course.timings} ({course.classroom})")
