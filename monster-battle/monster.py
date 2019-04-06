class monster():
    def __init__(self, name, height, weight, attack, defense):
        # Feed its own instance into itSELF
        # These are the user-selectable attributes
        self.name = name
        self.height = height
        self.weight = weight
        self.attack = attack
        self.defense = defense

        # We will compute the following attributes
        # Hit Points
        # Initiative
        # Chance to stun

        # Current state of the monster
        # Normal/stunned

    def attack(self):
        pass

    def defend(self, atk):
        pass
