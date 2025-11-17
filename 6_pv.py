class Hero:
    # class variabel
    jumlah = 0
    __privatejumlah = 0
    def __init__(self, name, health):
        self.name = name
        self.health = health
        
        # variabel instance private
        self.__private = "private"
        # variabel instance protected
        self._protected = "protected"
        
miya = Hero("Miya", 100)
print(miya.__dict__) 
print(Hero.__dict__)
# print(miya.health)