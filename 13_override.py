# override method

class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        
    def showinfo(self):
        print("showinfo di class hero")
        print("{} health : {}".format(self.name, self.health))
        
class Hero_itel(Hero):
    def __init__(self, name):
        super().__init__(name, 100)
        
    # override
    def showinfo(self):
        print("showinfo di sub class hero intel")
        print("{} \nTipe: intel, \nhealth: {}".format(
            self.name,
            self.health
        ))
        
class Hero_streng(Hero):
    def __init__(self, name):
        super().__init__(name,100)
        
chimi = Hero_itel('chimi')
misel = Hero_streng('misel')

misel.showinfo()
# misel.showinfo()