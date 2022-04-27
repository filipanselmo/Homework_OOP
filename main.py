from typing import Dict, Any


class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_in_progress = []
        self.grades = {}
        self.students = []



    def rate_ST(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


    def __str__(self):
        self.all_grades = []
        for grade in self.grades.values():
            self.all_grades.extend(grade)
            rating = sum(self.all_grades) / len(self.all_grades)

        return f'Имя: {self.name}'  '\n' f'Фамилия: {self.surname}' '\n' \
           f'Средняя оценка за домашнее задание: {round((rating),2)}' \
          '\n' f'Курсы с процессе изучения: {self.courses_in_progress}' '\n'\
          'Завершенные курсы: Введение в программирование'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.rating = []


    def __str__(self):
        self.all_grades = []
        for grade in self.grades.values():
             self.all_grades.extend(grade)
        rating = sum(self.all_grades) / len(self.all_grades)
        return f'Имя: {self.name}'  '\n' f'Фамилия: {self.surname}' \
             '\n' f'Средняя оценка за лекции: {round((rating),2)}'


    def __lt__(self,other):
         self.all_grades = []
         for grade in self.grades.values():
            self.all_grades.extend(grade)
         rating = sum(self.all_grades) / len(self.all_grades)
         return self.rating > other.rating


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


    def __str__(self):
        return f'Имя: {self.name}'  '\n' f'Фамилия: {self.surname}'




first_student = Student('Ruoy', 'Eman')
first_student.courses_in_progress += ['Python']
first_student.courses_in_progress += ['GIT']

second_student = Student('Ivan', 'Ivanov')
second_student.courses_in_progress += ['Python']
second_student.courses_in_progress += ['GIT']

cool_Reviewer = Reviewer('Some', 'Buddy')
cool_Reviewer.courses_attached += ['Python']
cool_Reviewer.courses_attached += ['GIT']

b_Reviewer = Reviewer('Petr', 'Petrov')
b_Reviewer.courses_attached += ['Python']
b_Reviewer.courses_attached += ['GIT']

cool_Reviewer.rate_hw(first_student, 'Python', 10)
cool_Reviewer.rate_hw(first_student, 'GIT', 9)

cool_Reviewer.rate_hw(second_student, 'Python', 4)
cool_Reviewer.rate_hw(second_student, 'GIT', 7)

b_Reviewer.rate_hw(first_student, 'Python', 8)
b_Reviewer.rate_hw(first_student, 'GIT', 3)

b_Reviewer.rate_hw(second_student, 'GIT', 7)
b_Reviewer.rate_hw(second_student, 'Python', 7)

cool_Lecturer = Lecturer('Semen', 'Semenov')
cool_Lecturer.courses_attached += ['Python']
cool_Lecturer.courses_attached += ['GIT']

m_Lecturer = Lecturer('Andrew', 'Kozlov')
m_Lecturer.courses_attached += ['Python']
m_Lecturer.courses_attached += ['GIT']

first_student.rate_ST(cool_Lecturer, 'Python', 7)
first_student.rate_ST(cool_Lecturer, 'GIT', 6)

first_student.rate_ST(m_Lecturer, 'Python', 3)
first_student.rate_ST(m_Lecturer, 'GIT', 7)

second_student.rate_ST(cool_Lecturer, 'Python', 5)
second_student.rate_ST(cool_Lecturer, 'GIT', 6)

second_student.rate_ST(m_Lecturer, 'Python', 4)
second_student.rate_ST(m_Lecturer, 'GIT', 10)
students_list = []
students_list.append(first_student.grades)
students_list.append(second_student.grades)

def av_st(student):
    all_ball=[]
    all_ball_2 = []
    for course in student.grades.values():
        all_ball.extend(student.grades.values())
        for grade in all_ball:
            all_ball_2.extend(grade)
            rating = sum(all_ball_2)/len(all_ball_2)
    return rating

def __lt__(first_student, second_student):
    return av_st(first_student)< av_st(second_student)
print(av_st(first_student)> av_st(second_student))


Lecturers_list = []
Lecturers_list.append(cool_Lecturer.grades)
Lecturers_list.append(m_Lecturer.grades)
def av_Lec(courses):
    av_ball = 0
    Lecturers_2 = []
    for dict in Lecturers_list:
        av_ball =sum(dict[courses])/len(dict[courses])
        Lecturers_2.append(av_ball)
    return sum(Lecturers_2)/len(Lecturers_2)
def __lt__(cool_Lecturer, m_Lecturer):
    return av_st(cool_Lecturer)< av_st(m_Lecturer)
print(av_st(cool_Lecturer)> av_st(m_Lecturer))
def average_homework_grades_by_course(students_list, course_name):
    grades_list = []
    counter = 0
    pre_result = 0
    for stud in students_list:
        grades_list.extend(stud[course_name])
    return sum(grades_list)/len(grades_list)

print(average_homework_grades_by_course(students_list,'Python'))

def average_homework_grades_by_course(Lecturers_list, course_name):
    grades_list = []
    counter = 0
    pre_result = 0
    for stud in Lecturers_list:
        grades_list.extend(stud[course_name])
    return sum(grades_list)/len(grades_list)

print(average_homework_grades_by_course(Lecturers_list,'Python'))


print(cool_Reviewer)
print(cool_Lecturer)
print(m_Lecturer)
print(b_Reviewer)
print(first_student)
print(second_student)