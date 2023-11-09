'''
File: OOP Assignment 2.py
Description: Main Code File for RPG OOP Assignment 2.
Author: Jirah Baker
StudentID: 110332584
EmailID: bakjg001
This is my own work as defined by the University's Academic Misconduct Policy.
'''

from abc import ABC, abstractmethod


class Alchemist:
    def __init__(self, attack, strength, defense, magic, ranged, necromancy, laboratory, recipies):
        self.attack = attack
        self.strength = strength 
        self.defense = defense
        self.magic = magic
        self.ranged = ranged
        self.necromancy = necromancy
        self.laboratory = Laboratory
        self.recipies = {}

class Laboratory:
    def __init__(self, potions, herbs, catalysts):
        self.potions = []
        self.herbs = []
        self.catalysts = []

class Potion(ABC):
    def __init__(self, name, stat, boost):
        self.name = name
        self.stat = stat
        self.boost = boost

class SuperPotion(Potion):
    def __init__(self, herb, catalyst, name, stat, boost):
        super().__init__(name, stat, boost)
        self.herb = herb
        self.cataylst = catalyst


class ExtremePotion(Potion):
    def __init__(self, reagent, potion, name, stat, boost):
        super().__init__(name, stat, boost)
        self.reagent = reagent
        self.potion = potion

class Reagent(ABC):
    def __init__(self, name, potency):
        self.name = name
        self.potency = potency

class Herb(Reagent):
    def __init__(self, grimy, name, potency):
        super().__init__(name, potency)
        self.grimy = True

class Catalyst(Reagent):
    def __init__(self, quality, name, potency):
        super().__init__(name, potency)
        self.quality = quality


