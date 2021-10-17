#!/c/Users/AngryBear/AppData/Local/Microsoft/WindowsApps/python
""" Написать класс Student, который инкапсулирует данные о студенте.

К параметрам каждого студента относятся:
1. Имя(строка не более 25 символов)
2. Фамилия(строка не более 50 символов)
3. Дата рождения(простая строка в формате DD.MM.YYYY)
4. Пол(два варианта значение - Male(Мужчина) или Female(Женщина))
5. Текущая оценка успеваемости(число от 0 до 10).
6. Специальность(строка не более 50 символов)
7. Номер курса(целое число)

Класс должен скрывать свои атрибуты от внешнего мира. Для доступа к ним необходимо использовать свойства. Список доступов
(ro - read only, rw - read/write):

Имя - ro
Фамилия - ro
Дата рождения - ro
Пол - ro
Текущая оценка - rw
Специальность - rw
Номер курса - rw

Реализуйте все необходимые свойства и атрибуты студента, выполнив при этом все необходимые проверки. В случае получения
невалидных данных необходимо возбуждать исключение ValueError(или можете создать свое собственное)."""

# https://www.w3schools.com/python/python_classes.asp
# https://habr.com/ru/post/444338/
# https://pythonworld.ru/osnovy/inkapsulyaciya-nasledovanie-polimorfizm.html
# https://pythonguide.readthedocs.io/en/latest/python/moreex.html#input-validation
# https://pythonguide.readthedocs.io/en/latest/python/moreex.html#generalized-validation
# http://www.easypythondocs.com/validation.html#definition

import time
# Класс Student с приватными и публичными атрибутами.
class Student:
    def __init__(self, name, sname, dob, gender, grade, speciality, course ):
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

# Валидация всех параметров.
def get_name():
    while True:
        name = input('input name ')
        if  len(name) > 25:
            print('wrong name')
            continue
        elif name.isdigit():
            print('wrong name')
            continue
        else:
            break
    return name

def get_sname():
    while True:
        sname = input('input sname ')
        if  len(sname) > 50:
            print('wrong sname')
            continue
        elif sname.isdigit():
            print('wrong sname')
            continue
        else:
            break
    return sname

def get_dob():
    while True:
        dob = input('input Date of Birth (dd/mm/yyyy) ')
        try:
            dob = time.strptime(dob, '%d/%m/%Y')
        except ValueError:
            print('wrong dob')
            continue
        else:
            break
    return dob

def get_gender():
    while True:
        gender = input('input gender ')
        if  gender == "female" or gender == "male":
            break
        else:
            print('wrong gender')
            continue
    return gender

def get_grade():
    while True:
        try:
            grade = int(input('input grade '))
        except ValueError:
            print('wrong number')
            continue
        if  grade > 10 or grade < 0:
            print('wrong number')
            continue
        else:
            break
    return grade

def get_course():
    while True:
        try:
            course = int(input('input course '))
        except ValueError:
            print('wrong number')
            continue
        if  course < 1:
            print('wrong number')
            continue
        else:
            break
    return course

def get_speciality():
    while True:
        speciality = input('input speciality ')
        if  len(speciality) > 50:
            print('wrong speciality')
            continue
        elif speciality.isdigit():
            print('wrong speciality')
            continue
        else:
            break
    return speciality

# Создание двух экземпляров класса для двух студентов.
studentOne = Student(get_name(), get_sname(), get_dob(), get_gender(), get_grade(), get_speciality(), get_course())
studentTwo = Student(get_name(), get_sname(), get_dob(), get_gender(), get_grade(), get_speciality(), get_course())

studentOne.all_attrs()
studentTwo.all_attrs()