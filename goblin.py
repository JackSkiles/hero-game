from lib.stats import Stats

class Goblin(Stats):
    def attack(self, target):
        target.health -= self.power