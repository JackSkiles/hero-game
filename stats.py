

class Stats():
    def __init__(self, health=50, power=10, name='goblin'):
        self.health = health
        self.power = power
        self.name = name

    def is_alive(self, target):
        if target.health > 0:
            target = True
        elif target.health <= 0:
            target = False
        return target
        
    def print_status(self, target):
        return (f"{target.name} has %d health and %d power." % (target.health, target.power))
            
    def attack(self, attacker, target):
        target.health -= attacker.power
        print(f'{attacker.name} does %d damage to {target.name}' % attacker.power)




