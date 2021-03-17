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

    def heal(self):
        self.health = (self.health + 4)

hero = Character(30, 6)

class Goblin(): #might be unneccecary, but if characater gets complicated later enemies should be based on character.
    def __init__(self):
        self.health = 10
        self.damage = 2

badGuy = Goblin()

def combat():
    action = input("type attack or heal!")
    if action == "attack":
        badGuy.health = badGuy.health - hero.damage
    elif action == "heal":
        hero.heal()
    else:
        print("invalid command, try again.")
        combat()
    
    if badGuy.health <= 0:
        print("you win!") # måste hoppa till en annan metod istället för att undvika repition.

        
    print("you currently have ", hero.health, " HP left, your enemy has ", badGuy.health, " HP left!")
    
    combat()

combat()