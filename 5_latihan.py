# latihan oop
# game sederhana

class Hero:
    
    def __init__(self, inputName, inputHealth, attackPower, armorNumber):
        self.name = inputName
        self.health = inputHealth
        self.attackPower = attackPower
        self.armorNumber = armorNumber
        
    def attack(self, lawan):
        print(self.name + ' menyerang ' + lawan.name)
        lawan.attacked(self, self.attackPower)
        
    def attacked(self, lawan, attackPower_lawan):
        print(self.name + ' diserang ' + lawan.name)
        attack_diterima = attackPower_lawan/self.armorNumber
        print("Serangan kena : " + str(attack_diterima))
        self.health -= attack_diterima
        print("Sisa Darah : " + self.name +  "tersisa " + str(self.health))
        
irithel = Hero('Irithel', 100, 50, 20)
granger = Hero('Granger', 100, 40, 30)

irithel.attack(granger)
print("="*20)
granger.attack(irithel)
