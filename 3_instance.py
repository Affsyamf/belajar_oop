class Hero:
    jumlah = 0
    def __init__(self, inputName, inputHealt, inputPower, inputArmor):
        # instance variabel
        self.name = inputName
        self.healt = inputHealt
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1
        print(f"Hero dengan nama : {inputName}")
        
hero1 = Hero ("granger", 100, 500, 70)
print(Hero.jumlah)
hero2 = Hero("esme", 2000, 100, 1000 )
print(Hero.jumlah)

    