#!/c/Users/AngryBear/AppData/Local/Microsoft/WindowsApps/python
#Rainbow = ['Red', 'Orange']
Rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
Fruits = ['Cherry', 'Orange', 'Banan', 'Apple']
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
