from lib.stats import Stats

class Zombie(Stats):
    def immortality(self):
        if self.health <= 0:
            self.health = 5
            print('you cannot kill a zombie')