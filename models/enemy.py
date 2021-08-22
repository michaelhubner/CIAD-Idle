import numpy
import math


class EnemyModel:

    def __init__(self, max_hp, defense):

        self.max_hp = max_hp
        self.hp = max_hp

        self.defense = defense
        self.is_alive = True

    def hit(self, damage):

        self.hp -= max(0, (damage - self.defense))

        if self.hp <= 0: self.is_alive = False

        print(f"Enemy got hit: ({self.max_hp},{self.hp})")


