class Group:
    """
    Class representing group in the university
    """

    def __init__(self, id, members):
        """
        Sets all the necessary attributes for the class Group
        :param id:
        :param members:
        """

        self.id = id
        self.members = members
        self.schedule = []


class Lecturer:
    """
    Class representing lecturers of the university
    """

    def __init__(self, id, name, courses):
        """
        Sets all the necessary attributes for the class Lecturer
        :param id:
        :param name:
        :param courses:
        """

        self.id = id
        self.name = name
        self.courses = courses
        self.availability = {}


class Course:
    """
    Class representing courses in the university
    """

    def __init__(self, id, name, lecturer, timings, classroom, group):
        """
        Sets all the necessary attributes for the class Course
        :param id:
        :param name:
        :param lecturer:
        :param timings:
        :param classroom:
        :param group:
        """

        self.id = id
        self.name = name
        self.lecturer = lecturer
        self.timings = timings
        self.classroom = classroom
        self.group = group


class Schedule:
    """
    Class representing schedule of lectures in group
    """

    def __init__(self, courses, timings):
        """
        Sets all the necessary attributes for the class Schedule
        :param courses:
        :param timings:
        """

        self.courses = courses
        self.timings = timings


def read_from_file(filename):
    """
    Function of reading data from the file
    :param filename:
    :return:
    """

    with open(filename, 'r', encoding='utf8') as f:
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
    """
    Function of getting group schedule
    :param group_id:
    :return: group schedule
    """

    groups, lecturers, courses = read_from_file('data.txt')
    return groups[group_id].schedule


def print_schedule(schedule):
    """
    Function of printing schedule
    :param schedule:
    :return:
    """

    for course in schedule:
        print(f"{course.name}: {course.timings} ({course.classroom})")
