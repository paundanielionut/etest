import numpy as np

from src.roles import Hero, WildBeast
from src.exceptions import HealthError


class Game:
    @staticmethod
    def determine_attacker(hero, wild_beast):
        if hero.speed > wild_beast.speed:
            hero.is_attacker = True
            wild_beast.is_attacker = False
        elif hero.speed < wild_beast.speed:
            hero.is_attacker = False
            wild_beast.is_attacker = True
        elif hero.luck > wild_beast.luck:
            hero.is_attacker = True
            wild_beast.is_attacker = False
        elif hero.luck < wild_beast.luck:
            hero.is_attacker = False
            wild_beast.is_attacker = True
        else:
            ch = np.random.choice([True, False])
            hero.is_attacker = ch
            wild_beast.is_attacker = not ch
    
    def play(self):
        """
        Game rules:
            1. determine attacker
            2. one attacks opponent with a damage
            3. opponet defend.
            4. switch roles
        """
        hero = Hero()
        wild_beast = WildBeast()

        Game.determine_attacker(hero, wild_beast)

        round = 1
        while round <= 20:
            print (f".................... round: {round} ..................\n")
            print(".... BEFORE .... ")
            print(f"{hero}")
            print(f"{wild_beast}")
            try:
                if hero.is_attacker:
                    print(f"{hero.name} attacks {wild_beast.name}!\n")
                    hero.attack(wild_beast)
                else:
                    print(f"{wild_beast.name} attacks {hero.name}!\n")
                    wild_beast.attack(hero)

                print(".... After .... ")
                print(f"{hero}")
                print(f"{wild_beast}")
                
            except HealthError as e:
                # End game
                print(e)
                print(f"{hero}")
                print(f"{wild_beast}")

                return

            round += 1


game = Game()

