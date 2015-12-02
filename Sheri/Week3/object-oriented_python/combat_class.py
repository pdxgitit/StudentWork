import random

class Combat(object):
    max_withstand_attack  = 30
    max_wounding_power = 30

    def fight(self):
        attack = random.randint(1, self.max_wounding_power)
        return attack

    def strength(self):
        wounding_power = random.randint(1, self.max_withstand_attack)
        return wounding_power
