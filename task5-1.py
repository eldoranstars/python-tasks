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

# Класс Student с приватными и публичными атрибутами.
class Student:
    def __init__(self, name, sname, dob, gender, grade, speciality, course ):
        self.name = name
        self.sname = sname
        self.dob = dob
        self.gender = gender
        self.grade = grade
        self.speciality = speciality
        self.course = course
    
    def __print_name(self):
        print(self.name)
    
    def __print_sname(self):
        print(self.sname)
    
    def __print_dob(self):
        print(self.dob)
    
    def __print_gender(self):
        print(self.gender)

    def print_grade(self):
        print(self.grade)

    def print_speciality(self):
        print(self.speciality)

    def print_course(self):
        print(self.course)

    # Функция вывода всех данных о студенте.
    def all_attrs(student_number):
        attrs = vars(student_number)
        print(', '.join("%s: %s" % item for item in attrs.items())) 

# Создание двух экземпляров класса для двух студентов.
studentOne = Student('Alex', 'Chistopolskiy', '01.01.1990', 'male', 5, 'mts', 'python')
studentTwo = Student('Max', 'Pain', '02.02.1990', 'male', 1, 'radio', 'cloud')

studentOne.all_attrs()
studentTwo.all_attrs()