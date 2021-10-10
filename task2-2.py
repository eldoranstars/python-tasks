#!/c/Users/AngryBear/AppData/Local/Microsoft/WindowsApps/python
#Написать скрипт, который определяет, является ли заданная строка полиндромом. Строку можно жестко задать в коде.
word = "abcba"
inversiya = word[::-1]
if word == inversiya:
    print('it is polindrom!')
else:
    print('it is not polindrom!')
