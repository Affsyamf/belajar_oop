class Hero:
    __jumlah = 0
    def __init__(self, name, health):
        self.name = name
        self.health = health
        Hero.__jumlah += 1
        
    # method hanya berlaku untuk objek
    def getJumlah(self):
        return Hero.__jumlah
    
    # method ini tidak berlaku untuk objek tapi berlaku untuk class
    def getJumlah1():
        return Hero.__jumlah
    
    # method static (decorator) nempel ke objek atau class
    @staticmethod
    def getJumlah2():
        return Hero.__jumlah
    
    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah
        
    
miya = Hero ("miya", 100)
print(Hero.getJumlah2())
ranger = Hero("ranger", 100)
print(ranger.getJumlah2())
raya = Hero("Raya", 80)
print(raya.getJumlah3())