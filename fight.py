import random


class Person:

    def __init__(self, name, strength, agility) -> None:
        self.name = name
        self.strength = strength
        self.agility = agility
        self.actual_hp = self.hp = strength * 15
        print(f'There is {self.name} with {self.actual_hp} hp')
        

class Enemy(Person):
    attack_types = {'punch to face': 3} #name of attack and damage  


class Hero(Person):
     attack_types = {'hit to face': 3, 'hit to balls': 5}


class Fight:
    def __init__(self, hero, enemy):
        self.hero = hero
        self.enemy = enemy

    def _perform_attack(self, attaker, defender):
        hit_name, hit_damage = random.choice(list(attaker.attack_types.items()))   
        hit = (attaker.strength + hit_damage) * random.randint(2,4)
        #base on agility * on number from 1 to 3 warrior that take hit have chance to avoit it
        miss_chance = defender.agility * random.randint(1,3) >=  attaker.agility * random.randint(1,3)
        if miss_chance:
            print(f'{attaker.name} missed')
        else:
            defender.actual_hp -= hit
            print(f"{attaker.name} did {hit_name} {defender.name} with {hit} damage. Now {defender.name} hp is {max(defender.actual_hp, 0) }")


    def fight(self):
        print('The fight is started')
        print(f'{self.hero.name} hp is {self.hero.hp}, {self.enemy.name} hp is {self.enemy.hp}')
        while self.hero.actual_hp > 0 and self.enemy.actual_hp > 0: 
            #warriors_order deside who will hit first in this round 
            warriors_order = [self.hero, self.enemy] if self.hero.agility * random.randint(1,3) >= self.enemy.agility * random.randint(1,3) else [self.enemy, self.hero]
            print(f'{warriors_order[0].name} was faster')             
            self._perform_attack(warriors_order[0], warriors_order[1])
            if warriors_order[1].actual_hp > 1:
                self._perform_attack(warriors_order[1], warriors_order[0])
            
        winner = self.hero.name if self.hero.actual_hp > 0 else self.enemy.name
        print(f'{winner} wins the battle')

        
if __name__ == "__main__":
    hero = Hero('Hero', 5, 8)
    number_of_enemies = random.randint(1, 3)
    list_of_enemies = [Enemy(
        f'drunk Buddy{i}',
        random.randint(4, 6),
        random.randint(4, 6)
        ) for i in range(number_of_enemies) ]

    print(f"You have {len(list_of_enemies)} enemies.")
    for enemy in list_of_enemies:
        print('--------------')
        if hero.actual_hp > 0:              
            Fight(hero, enemy).fight()
        else:
            print("you don't have power to continue")
            break
            



