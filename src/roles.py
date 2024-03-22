import numpy as np

from src.exceptions import HealthError


class Character:
    def __init__(self, name, health, strength, defence, speed, luck, is_attacker=False):
        self.name = name
        self.health = health
        self.strength = strength
        self.defence = defence
        self.speed = speed
        self.luck = luck
        self.is_attacker = is_attacker

    def get_damage(self, opponent):
        """
        if self is instance of hero -> he can use rapid_strike -> damage *=2 
        otherwise damage will have default value.
        """
        damage = self.strength - opponent.defence

        # if opponent is more lucky than me -> damage will be 0
        # if opponent.luck > self.luck:
        #     damage = 0
            
        if isinstance(self, Hero):
            rapid_strike = np.random.randint(0, 100)

            if rapid_strike <= 10: 
                print(f"{self.name} is using rapid strike!")
                return damage*2
            return damage
        elif isinstance(self, WildBeast):
            return damage
    
    def attack(self, opponent):
        damage = self.get_damage(opponent)
               
        print(f"opponent's damage = {damage} \n")
        opponent.defend(self, damage)

        # switch roles
        self.is_attacker = False
        opponent.is_attacker = True

    def defend(self, opponent, damage):
        if isinstance(self, Hero):
            magic_shield = np.random.randint(0, 100)

            if magic_shield <= 20:
                print(f"{self.name} is using magic shield!")
                self.health = self.health - damage//2
            else:
                self.health = self.health - damage
        elif isinstance(self, WildBeast):
            self.health = self.health - damage
        
        if self.health <= 0:
            raise HealthError(
                ".... end game! ....\n"
                f".... {opponent.name} wins! ...."
            )

    def __str__(self):
        return (
            f"name: {self.name}\n"
            f"health: {self.health}\n"
            f"strength: {self.strength}\n"
            f"defence: {self.defence}\n"
            f"speed: {self.speed}\n"
            f"luck: {self.luck}\n"
            f"is_attacker: {self.is_attacker}\n"
        )
            

class Hero(Character):
    def __init__(self):
        super(Hero, self).__init__(
            name="Orderus",
            health=np.random.randint(70, 100),
            strength=np.random.randint(70, 80),
            defence=np.random.randint(45, 55),
            speed=np.random.randint(40, 50),
            luck=np.random.uniform(0.10, 0.30)
        )


class WildBeast(Character):
    def __init__(self):
        super(WildBeast, self).__init__(
            name="WildBeast",
            health=np.random.randint(60, 90),
            strength=np.random.randint(60, 90),
            defence=np.random.randint(40, 60),
            speed=np.random.randint(40, 60),
            luck=np.random.uniform(0.25, 0.40)
        )
        
