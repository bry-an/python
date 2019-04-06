from time import sleep
from num2words import num2words
from monster import monster


def create_monster(pos):
    # TODO: BETTER INPUT VALIDATION!!!
    # Name
    name = input(
        f"Enter a name for the {num2words(pos, to='ordinal')} monster: ")
    # Height
    height = int(input(f"  How tall is {name} (1-10)? "))
    # Weight
    weight = int(input(f"  How much does {name} weigh (50-150)? "))
    # Damage
    damage = int(input(f"  How hard does {name} hit (1-10)? "))
    # Defense
    defense = int(
        input(f"  How much damage can {name} absorb at once (1-10)? "))
    this_monster = monster(name, height, weight, damage, defense)
    return this_monster


def turn_tracker(A, B):
    '''Generates a sequence of turns, given two initiatives

    Input: Two initiatives (i) such that 1 <= i <= 100
    Output: Sequence of turns, 0==A, 1==B'''

    # Initialize a counter and a "double" tracker
    c, dbl = 1, False
    while True:
        if c % A == 0 and c % B == 0:
            # Both monsters attack during this "clock tick"
            yield int(dbl)
            dbl = not dbl
        elif c % A == 0:
            # Only monster A attacks
            yield 0
        elif c % B == 0:
            # Only monster B attacks
            yield 1
        if not dbl:
            c = c % 100 + 1
        # Note: This generator will frequently loop without yielding a result


def battle(*monst):

    turn = turn_tracker(monst[0].initiative, monst[1].initiative)

    lw = sum(len(str(m.hit_points)) for m in monst) + 4
    rw = max(len(str(m.name)) for m in monst) + 12

    while monst[0].alive() and monst[1].alive():
        attacker = next(turn)
        defender = not attacker
        attack_data = monst[attacker].attack()
        status = f"{monst[0].hit_points} <> {monst[1].hit_points}".ljust(lw)
        if attack_data['stun']:
            status += f" : {monst[defender].name} stunned!".rjust(rw)
        else:
            status += "".rjust(rw)
        print(status, end='\r', flush=True)
        monst[defender].defend(**attack_data)
        sleep(.2)

    print('')

    print(f"{monst[0].name if monst[0].alive() else monst[1].name} wins!")


if __name__ == "__main__":
    print('Welcome to Monster Battle!')
    # monster_one = create_monster(1)
    # monster_two = create_monster(2)
    monster_one = monster('a', 3, 50, 3, 3)
    monster_two = monster('b', 3, 50, 3, 3)
    print(monster_one)
    print(monster_two)
    battle(monster_one, monster_two)
    pass
