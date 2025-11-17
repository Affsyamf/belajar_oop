class Hero:
    def __init__(self,name,health):
        self.name = name
        self.health = health
    
    def showinfo (self):
        print("{} dengan health: {}".format(self.name, self.health))
        
class hero_intel(Hero):
    def __init__(self, name):
        # Hero.__init__(self, name, 100)
        super().__init__(name, 100)
        super().showinfo()

class hero_streng(Hero):
    def __init__(self, name):
        super().__init__(name, 200)
        super().showinfo()
        
dira = hero_intel('dira')
amira = hero_streng('amira')
