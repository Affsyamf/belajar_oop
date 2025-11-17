class Hero: 
    pass

hero1 = Hero()
hero2 = Hero()
hero3 = Hero()

hero1.name = "granger"
hero1.attack = 100

hero2.name = "miya"
hero2.attack = 300

hero3.name = "esme"
hero3.attack = 70

print(f"Nama hero 1 : {hero1.name}")
print(hero1.__dict__)