# class super
class Hero: 
    
    def __init__(self, name, health):
        self.name = name
        self.health = health
       
# sub class 
class Hero_inteligent(Hero):
    pass

class Hero_streng(Hero):
    pass

miya = Hero('miya', 100)
hana = Hero_inteligent('hana', 50)
axe = Hero_streng('axe', 1000)
print(miya.name)
print(hana.name)
print(axe.name)