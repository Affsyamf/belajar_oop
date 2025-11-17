class Hero:
    def __init__(self, name, health, attackPower):
        self.__name = name
        self.__health = health
        self.__attpower = attackPower

    # getter
    def getName(self):
        return self.__name 
    
    def getHealth(self):
        return self.__health
    
    # setter
    def diserang(self, damage):
        self.__health -= damage
    
# awal game 
claude = Hero("Claude", 100, 5)

# game berjalan
print(claude.getName())
print(claude.getHealth())
claude.diserang(5)
print(claude.getHealth())