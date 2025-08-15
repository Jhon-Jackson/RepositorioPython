class Character:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def attack(self):
        print(f"{self.name} attacks with um basic strike")


class Warrior(Character):
    def attack(self):
        print(f"{self.name} swings a sword with strength level {self.level}!")


class Mage(Character):
    def attack(self):
        print(f"{self.name} casts a fireball with power level {self.level}!")

c1 = Warrior("Falcao", 15)
c2 = Mage("Falcone", 17)

c1.attack()
c2.attack()