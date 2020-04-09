from lib.stats import Stats

class Hero(Stats):
    def increase_health(self, health_up):
        lives = 5
        while lives <= 0:
            if self.health <= 0:
               self.health = 10
            lives -= 1

    def __repr__(self):
        print(f'heros health is: {self.health}')
    
    
    # def attack(self, target):
    #     target.health = target.health - self.power
