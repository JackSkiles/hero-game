from lib.stats import Stats

class Hero(Stats):
    def increase_health(self, health_up):
        if self.health <= 0:
            self.health = 10

    def __repr__(self):
        print(f'heros health is: {self.health}')