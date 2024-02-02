import random


class Person:

    def __init__(self, name, strength, agility) -> None:
        self.name = name
        self.strength = strength
        self.agility = agility
        self.actual_hp = self.hp = strength * 15
        print(f'{self.name} {self.actual_hp} {self.hp}')
        

class Enemy(Person):
    attack_types = {'punch to face': 3} #name of attack and damage  


class Hero(Person):
     attack_types = {'hit to face': 3, 'hit to balls': 5}


class Fight:
    def __init__(self, hero, enemy):
        self.hero = hero
        self.enemy = enemy

    def fight(self):
        print('The fight is started')
        print(f'{self.hero.name} hp is {self.hero.hp}, {self.enemy.name} hp is {self.enemy.hp}')
        while True: 
            #warriors_order deside who will hit first in this round 
            warriors_order = [self.hero, self.enemy] if self.hero.agility * random.randint(1,3) >= self.enemy.agility * random.randint(1,3) else [self.enemy, self.hero]
            print(f'{warriors_order[0].name} was faster')  

            #base on strength * on number from 3 to 6 warrior that act first provide a hit     
            hit_name, hit_damage = random.choice(list(warriors_order[0].attack_types.items()))   
            hit = (warriors_order[0].strength + hit_damage) * random.randint(2,4)
            #base on agility * on number from 1 to 3 warrior that take hit have chance to avoit it
            miss_chance = warriors_order[1].agility * random.randint(1,3) >=  warriors_order[0].agility * random.randint(1,3)
            if miss_chance:
                print(f'{warriors_order[0].name} missed')
            else:
                warriors_order[1].actual_hp -= hit
                print(f"{warriors_order[0].name} did {hit_name} {warriors_order[1].name} with {hit} damage. Now {warriors_order[1].name} hp is {warriors_order[1].actual_hp if warriors_order[1].actual_hp >= 0 else 0}")
            if warriors_order[1].actual_hp > 1:
                #the same logic for second warrior if he still alive
                hit_name, hit_damage = random.choice(list(warriors_order[1].attack_types.items()))   
                hit = (warriors_order[1].strength + hit_damage) * random.randint(2,4)
                miss_chance = warriors_order[0].agility * random.randint(1,3) >=  warriors_order[1].agility * random.randint(1,3)
                if miss_chance:
                    print(f'{warriors_order[1].name} missed')
                else:
                    warriors_order[0].actual_hp -= hit
                    print(f"{warriors_order[1].name} did {hit_name} {warriors_order[0].name} with {hit} damage. Now {warriors_order[0].name} hp is {warriors_order[0].actual_hp if warriors_order[0].actual_hp >= 0 else 0}")

            if self.hero.actual_hp < 1 or self.enemy.actual_hp < 1:
                break

            
        print(f'{self.hero.name} win'if self.hero.actual_hp > 0 else f'{self.hero.name}  lose')



hits_type = {'punch to face': 0, 'hit to face': 0, 'hit to balls': 0}

hero = Hero('Hero', 5, 5)
enemy1 = Enemy('Drank Hurry', 5, 6)

Fight(hero, enemy1).fight()




