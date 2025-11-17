class Hero:
    def __init__(self, inputName, inputHealt, inputPower, inputArmor):
        self.name = inputName
        self.healt = inputHealt
        self.power = inputPower
        self.armor = inputArmor
        
hero1 = Hero ("granger", 100, 500, 70)
hero2 = Hero("esme", 2000, 100, 1000 )

print(hero1.__dict__)
print(hero2.__dict__)
    