class Hero:
    jumlah_hero = 0
    
    def __init__(self, inputName, inputHealth, inputAttack, inputArmor):
        # instance variabel
        self.name = inputName
        self.health = inputHealth
        self.attack = inputAttack
        self.armor = inputArmor
        Hero.jumlah_hero += 1
     
    # method tanpa return, tanpa argumen
    def saya(self):
        print(f"Nama saya hero : {self.name}")

    # method dengan argumen
    def healthup(self,up):
        self.health += up
    
    # method dengan return
    def gethealth(self):
        return self.health
    
    
hero1 = Hero('irithel', 100, 700, 80)
hero2 = Hero('badang', 1000, 90, 500)
print(hero1.name)
hero1.saya()
hero2.saya()
hero1.healthup(20)
print(hero1.gethealth())