"""
TODO:
character class - 
stats: have HP, EXP, Damage.
Methods: attack, heal.

Enemy: HP, Damage.
Always attacks

Combat:
1. Player chooses 1 action
2. enemy attacks
3. Repeat until either is dead.

LEVEL UP:
After combat, character gains exp
every 10 exp, let's player gain 2 hp or 1 damage.

"""

class Character:
    def __init__(self, hp, d):
        self.health = hp
        self.damage = d

hero = Character(15, 3)

class Goblin(Character): #might be unneccecary, but if characater gets complicated later enemies should be based on character.
    def __init__(self):
        self.health = 8
        self.damage = 2