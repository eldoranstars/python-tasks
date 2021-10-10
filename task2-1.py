#!/c/Users/AngryBear/AppData/Local/Microsoft/WindowsApps/python
#Есть два списка разной длины. В первом содержатся ключи, а во втором значения. Напишите функцию, которая создаёт из этих ключей и значений словарь. Если ключу не хватило значения, в словаре должно быть значение None. Значения, которым не хватило ключей, нужно игнорировать.
#Rainbow = ['Red', 'Orange']
Rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
Fruits = ['Cherry', 'Orange', 'Banan', 'Apple']
def make_dict():    
    lengthRainbow = len(Rainbow)
    lengthFruits = len(Fruits) 
    if lengthRainbow > lengthFruits:
        difference = lengthRainbow - lengthFruits
        i = 0
        while i < difference:
            Fruits.append("None")
            i+=1
    if lengthRainbow < lengthFruits:
        difference = lengthFruits - lengthRainbow
        i = 0
        while i < difference:
            Fruits.pop()
            i+=1
    RainbowAndFruits = dict(zip(Rainbow,Fruits))
    print(RainbowAndFruits)
make_dict()
