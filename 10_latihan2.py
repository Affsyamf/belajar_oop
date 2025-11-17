# latihan enkapsulasi
class Hero:
    
    __jumlah = 0
    def __init__(self, name, health, attackPower, armorNumber, ):
        self.__name = name
        self.__healthStandar = health
        self.__attPowerStandar = attackPower
        self.__armorStandar = armorNumber
        self.__level = 1
        self.__exp = 0
        
        self.__healthMax = self.__healthStandar * self.__level
        self.__attackPower = self.__attPowerStandar * self.__level
        self.__armorNumber = self.__armorStandar * self.__level
        
        self.__health = self.__healthMax
        
        Hero.__jumlah += 1
        
    @property
    def info (self):
        return "{} level {}: \nHealth = {}/{} \nAttack = {} \nArmor = {}".format(self.__name, self.__level, self.__health, self.__healthMax, self.__attackPower, self.__armorNumber)

    @property
    def gainExp(self):
        pass
    
    @gainExp.setter
    def gainExp(self,addExp):
        self.__exp += addExp
        if (self.__exp >= 100):
            print(self.__name, "level up")
            self.__level += 1
            self.__exp -= 100
        
            self.__healthMax = self.__healthStandar * self.__level
            self.__attackPower = self.__attPowerStandar * self.__level
            self.__armorNumber = self.__armorStandar * self.__level
        
    def attack(self,musuh):
        self.gainExp = 50
      
        
raja = Hero('Raja', 100, 5, 10)
ratu = Hero('ratu', 100, 5, 10)
print(raja.info)

raja.attack(ratu)
raja.attack(ratu)
raja.attack(ratu)
print(raja.info)