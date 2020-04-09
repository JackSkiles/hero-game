

class Stats():
    def __init__(self, health=50, power=10, name='goblin'):
        self.health = health
        self.power = power

    def is_alive(self, target):
        if target.health > 0:
            target = True
        elif target.health <= 0:
            target = False
        return target
    def print_status(self, target)
    print("You have %d health and %d power." % (cloud.health, cloud.power))
        print("The goblin has %d health and %d power." % (goblin.health, goblin.power))
            




