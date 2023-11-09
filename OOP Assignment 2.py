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
        self.__attack = attack
        self.__strength = strength 
        self.__defense = defense
        self.__magic = magic
        self.__ranged = ranged
        self.__necromancy = necromancy
        self.__laboratory = Laboratory
        self.__recipies = {}

class Laboratory:
    def __init__(self, potions, herbs, catalysts):
        self.__potions = []
        self.__herbs = []
        self.__init__catalysts = []

class Potion(ABC):
    def __init__(self, name, stat, boost):
        self.__name = name
        self.__stat = stat
        self.__boost = boost

class SuperPotion(Potion):
    def __init__(self, herb, catalyst, name, stat, boost):
        super().__init__(name, stat, boost)
        self.__herb = herb
        self.__cataylst = catalyst


class ExtremePotion(Potion):
    def __init__(self, reagent, potion, name, stat, boost):
        super().__init__(name, stat, boost)
        self.__reagent = reagent
        self.__potion = potion

class Reagent(ABC):
    def __init__(self, name, potency):
        self.__name = name
        self.__potency = potency

class Herb(Reagent):
    def __init__(self, grimy, name, potency):
        super().__init__(name, potency)
        self.__grimy = True

class Catalyst(Reagent):
    def __init__(self, quality, name, potency):
        super().__init__(name, potency)
        self.__quality = quality


