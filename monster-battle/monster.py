from math import ceil
from random import randint


class monster():

    def __init__(self, name, height, weight, damage, defense):
        # These are the user-selectable attributes
        self.name = name
        self.height = height
        self.weight = weight
        self.damage = damage
        self.defense = defense

        # We will compute the following attributes
        # Hit Points
        self.hit_points = int((1.5 * self.height) *
                              (.75 * self.weight) * (1.2 * self.defense))
        # Initiative
        # This should be an integer in the 1-100 range, given our desired input ranges
        self.initiative = ceil((self.height * self.weight) / 15)
        # Chance to stun
        # This should be a float between .005 and .5
        self.stun_chance = round(.05 * self.damage / self.defense, 5)

        # Current state of the monster
        # Normal/stunned
        self.stunned = False

    def __str__(self):
        return f"""{self.name}
      Height: {self.height}
      Weight: {self.weight}
      Damage: {self.damage}
      Defense: {self.defense}
      Initiative: {self.initiative}
      Stun Chance: {self.stun_chance:.3%}
      Current Status: {'*** Stunned ***' if self.stunned else 'Ready'}
      Current Hit Points: {self.hit_points}"""

    def attack(self):
        if self.stunned:
            self.stunned = False
            return {'dmg': 0, 'stun': False}
        else:
            stun = randint(0, 999)/1000 <= self.stun_chance
            return {'dmg': self.damage, 'stun': stun}

    def defend(self, dmg, stun):
        if stun:
            self.stunned = True
        self.hit_points -= ceil(10 * dmg / self.defense)

    def alive(self):
        return self.hit_points > 0
