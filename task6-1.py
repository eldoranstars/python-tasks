#!/c/Users/AngryBear/AppData/Local/Microsoft/WindowsApps/python
# Необходимо написать скрипт, который будет загружать students.dat, парсить его и возвращать 
# данные в виде класса ExtendedStudent порожденного от разработанного в задании 5 класса Student.  
# Данный класс(ExtenderStudent) добавляет в класс Student новое поля:  login и password.
# После загрузки файла, скрипт должен сгенерить логины для всех студентов в формате:
# <Первая буква имени><фамилия>[order_no], где order_no – порядковый номер, который не является обязательным.
# Так же он должен генерировать пароль для каждого юзера случайным образом – не менее 6 
# и не более 9 символов в разном регистре или цифр. Тут вам поможет модуль random и модуль string.
# И наконец скрипт записывает получившиеся данные по студентам в файл ext_students.dat в произвольном(на ваш выбор) формате.

# https://www.vipinajayakumar.com/parsing-text-with-python/

my_string = 'Ivan:::Ivanov:::1980-11-11:::M:::1:::Developer:::2'
StID = my_string.split(':::')

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

ExtendedStudent = Student(StID[0], StID[1], StID[2], StID[3], StID[4], StID[5], StID[6])
ExtendedStudent.all_attrs()