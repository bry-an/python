from monster import monster
from num2words import num2words


def create_monster(pos):
    # Name
    name = input(
        f"Enter a name for the {num2words(pos, to='ordinal')} monster: ")
    # Height
    height = input(f"  How tall is {name} (1-10)? ")
    # Weight
    weight = input(f"  How much does {name} weigh (50-150)? ")
    # Damage
    damage = input(f"  How hard does {name} hit (1-10)? ")
    # Defense
    defense = input(f"  How much damage can {name} absorb at once (1-10)? ")

    new_monster = monster(name, height, weight, damage, defense)

    return new_monster


def battle(monster_one, monster_two):
    pass


if __name__ == "__main__":
    print('Welcome to Monster Battle!')
    monster_one = create_monster(1)
    monster_two = create_monster(2)
    pass
