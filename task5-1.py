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

#https://www.w3schools.com/python/python_classes.asp

class Student:
  def __init__(self, name, sname, dob, gender, grade, speciality, course ):
    self.name = name
    self.sname = sname
    self.dob = dob
    self.gender = gender
    self.grade = grade
    self.speciality = speciality
    self.course = course

studentOne = Student('Alex', 'Chistopolskiy', '01.01.1990', 'male', '5', 'mts', 'python')