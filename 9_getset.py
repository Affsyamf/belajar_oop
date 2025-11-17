class Hero:
    def __init__(self, name, health, armor):
        self.name = name
        self.__health = health
        self.__armor = armor
        # self.__info =  "name {} : \nhealth: {} \narmor: {} ".format(self.__name,self.__health,self.__armor) 
        
    @property
    def info(self):
        return "name {} : \nhealth: {} \narmor: {} ".format(self.name,self.__health,self.__armor) 
        
    @property
    def armor(self):
        pass
    
    @armor.getter
    def armor(self):
        return self.__armor
      
    @armor.setter  
    def armor(self, input):
        self.__armor = input
        
    @armor.deleter
    def armor(self):
        print("Armor di hapus")
        self.__armor = None
    
    
dadan = Hero("dadan", 100,10)

print("merubah info")
print(dadan.info)

dadan.name = "luis"
print(dadan.info)

print("getter dan setter untuk __armor : ")
print(dadan.armor)

dadan.armor = 50
print(dadan.armor)

print("delete armor")
del dadan.armor
print(dadan.armor)
print(dadan.__dict__)