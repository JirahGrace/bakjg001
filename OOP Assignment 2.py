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
        self.potions = Potion
        self.herbs = Herb
        self.catalysts = Catalyst

class Potion(ABC):
    def __init__():

class SuperPotion(Potion):
    pass

class ExtremePotion(Potion):
    pass

class Reagent(ABC):
    pass

class Herb(Reagent):
    pass

class Catalyst(Reagent):
    pass


