#!/c/Users/AngryBear/AppData/Local/Microsoft/WindowsApps/python
# Необходимо написать скрипт, который будет загружать students.dat, парсить его и возвращать 
# данные в виде класса ExtendedStudent порожденного от разработанного в задании 5 класса Student.  
# Данный класс(ExtendedStudent) добавляет в класс Student новое поля:  login и password.
# После загрузки файла, скрипт должен сгенерить логины для всех студентов в формате:
# <Первая буква имени><фамилия>[order_no], где order_no – порядковый номер, который не является обязательным.
# Так же он должен генерировать пароль для каждого юзера случайным образом – не менее 6 
# и не более 9 символов в разном регистре или цифр. Тут вам поможет модуль random и модуль string.
# И наконец скрипт записывает получившиеся данные по студентам в файл ext_students.dat в произвольном(на ваш выбор) формате.
# https://www.vipinajayakumar.com/parsing-text-with-python/
# https://www.pythontutorial.net/python-basics/python-read-text-file/
# https://python-scripts.com/random

import random 

class Student():
    def __init__(self, name, sname, dob, gender, grade, speciality, course):
        self.__name = name
        self.__sname = sname
        self.__dob = dob
        self.__gender = gender
        self.grade = grade
        self.speciality = speciality
        self.course = course

    # Функция вывода всех данных о студенте.
    def all_attrs(st_num):
        #attrs = vars(st_num)
        #print(', '.join("%s: %s" % item for item in attrs.items())) 
        print(st_num.__name, st_num.__sname, st_num.__dob, st_num.__gender, st_num.grade, st_num.speciality, st_num.course)

class ExtendedStudent(Student):
    def login(self):
        return '_Student__login: ' + ExtendedStudentID._Student__name[0] + ExtendedStudentID._Student__sname
    def password(self):
        city_list = ['Moscow', 'Vegas', 'Chicago', 'Houston', 'Philadelphia']
        return '_Student__password: ' + random.choice(city_list) + str(random.randint(0, 99))

    # Функция вывода всех данных о студенте.
    def all_ext_attrs(st_num):
        attrs = vars(st_num)
        login = ExtendedStudentID.login()
        password = ExtendedStudentID.password()
        print(', '.join("%s: %s" % item for item in attrs.items()), login, password)
        #print(st_num.__name, st_num.__sname, st_num.__dob, st_num.__gender, st_num.grade, st_num.speciality, st_num.course, st_num.login)

with open('students.dat') as f:
    for line in f:
        StID = line.split(':::')
        ExtendedStudentID = ExtendedStudent(StID[0], StID[1], StID[2], StID[3], StID[4], StID[5], StID[6])
        ExtendedStudentID.all_ext_attrs()
        
        #ext = open('ext_students.dat', 'w')
        #ext.write(str(ExtendedStudentID.all_ext_attrs()) + '\n')
        #ext.close()