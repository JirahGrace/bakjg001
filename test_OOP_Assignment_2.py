'''
File: test_OOP Assignment 2.py
Description: Test Code File for RPG OOP Assignment 2.
Author: Jirah Baker
StudentID: 110332584
EmailID: bakjg001
This is my own work as defined by the University's Academic Misconduct Policy.
'''

import unittest
from OOP_Assignment_2 import *

class TestAlchemist(unittest.TestCase):
    def testGetLaboratory(self):
        pass

    def testGetRecipies(self):
        pass

    def testMixPotion(self):
        alchemist = Alchemist(1, 1, 1, 1, 1, 1, Laboratory([],[],[]))
        # Add required herbs.
        alchemist.collectReagent(Herb("Irit", 1.0), 10)
        alchemist.collectReagent(Herb("Kwuarm",1.2), 10)
        alchemist.collectReagent(Herb("Cadantine", 1.5), 10)
        alchemist.collectReagent(Herb("Lantadyme", 2.0), 10)
        alchemist.collectReagent(Herb("Dwarf Weed", 2.5), 10)
        alchemist.collectReagent(Herb("Arbuck", 2.6), 10)
        alchemist.collectReagent(Herb("Avantoe", 3.0), 10)
        alchemist.collectReagent(Herb("Torstol", 4.5), 10)
        # Add required catalysts.
        alchemist.collectReagent(Catalyst("Eye of Newt", 4.3, 1.0), 10)
        alchemist.collectReagent(Catalyst("Limpwurt Root", 3.6, 1.7), 10)
        alchemist.collectReagent(Catalyst("White Berries", 1.2, 2.0), 10)
        alchemist.collectReagent(Catalyst("Potato Cactus", 7.3, 0.1), 10)
        alchemist.collectReagent(Catalyst("Wine of Zamorak", 1.7, 5.0), 10)
        alchemist.collectReagent(Catalyst("Blood of Orcus", 4.5, 2.2), 10)
        alchemist.collectReagent(Catalyst("Ground Mud Rune", 2.1, 6.7), 10)
        alchemist.collectReagent(Catalyst("Grenwall Spike", 6.3, 4.9), 10)
        alchemist.collectReagent(Catalyst("Ground Miasma Rune",3.3, 5.2), 10)
        # Mix.
        print("-" * 40 + "Mix Potions from Recipes" + "-" * 40)
        for recipe in alchemist.getRecipies():
            alchemist.mixPotion(recipe) 

        self.assertEqual(len(alchemist.getLaboratory().getPotions()), 6)


    def testDrinkPotion(self):
        pass

    def testCollectReagent(self):
        pass

    def testRefineReagent(self):
        herb = Herb("test", 10)
        catalyst = Catalyst("Dog", 7, 5)
        alchemist = Alchemist(0, 0, 0, 0, 0, 0, Laboratory([], [], []))
        alchemist.collectReagent(herb, 1)
        alchemist.collectReagent(catalyst, 1)
        alchemist.refineReagents()
        self.assertEqual(alchemist.getLaboratory().getHerbs()[0].getPotency(), 25.0)
        self.assertEqual(alchemist.getLaboratory().getCatalysts()[0].getQuality(), 6.1)


class TestLaboratory(unittest.TestCase):
    def testMixPotion(self):
        lab = Laboratory([], [], [])
        herb = Herb("test", 10)
        lab.addReagent(herb, 10)
        catalyst = Catalyst("Dog", 7, 5)
        lab.addReagent(catalyst, 3)
        lab.mixPotion("TestPotion", "Don't Care", "Magic", "test", "Dog")
        self.assertEqual(len(lab.getPotions()), 1)
        lab.mixPotion("TestExtreme", "Don't Care", "Extreme", "test", "TestPotion")
        self.assertEqual(len(lab.getPotions()), 1)

    def testAddReagent(self):
        herb = Herb("test", 10)
        lab = Laboratory([], [], [])
        lab.addReagent(herb, 10)
        self.assertEqual(len(lab.getHerbs()), 10)
        catalyst = Catalyst("Dog", 7, 5)
        lab.addReagent(catalyst, 3)
        self.assertEqual(len(lab.getCatalysts()), 3)


class TestPotion(unittest.TestCase):
    def testGetName(self):
        pass

    def testGetStat(self):
        pass

    def testGetBoost(self):
        pass

    def testSetBoost(self):
        pass


class TestSuperPotion(unittest.TestCase):
    def testCalculateBoost(self):
        herb = Herb("test", 10)
        catalyst = Catalyst("Dog", 7, 5)
        superPotion = SuperPotion(herb, catalyst, "testPotion", "stat", -1.0)
        self.assertEqual(superPotion.calculateBoost(), (10 + (7*5)*1.5))
        

    def testGetHerb(self):
        pass

    def testGetCatalyst(self):
        pass


class TestExtremePotion(unittest.TestCase):
    def testCalculateBoost(self):
        herb = Herb("test", 10)
        catalyst = Catalyst("Dog", 7, 5)
        superPotion = SuperPotion(herb, catalyst, "testPotion", "stat", -1.0)
        extremePotion = ExtremePotion(catalyst, superPotion, "Test", False, 1)
        self.assertEqual(extremePotion.calculateBoost(), 21.0)

    def testGetReagent(self):
        pass

    def testGetPotion(self):
        pass


class TestReagent(unittest.TestCase):
    def testGetName(self):
        pass

    def testGetPotency(self):
        pass

    def testSetPotency(self):
        pass


class TestHerb(unittest.TestCase):
    def testRefine(self):
        herb = Herb("test", 10)
        before = herb.getPotency()
        herb.refine()
        self.assertEqual(herb.getPotency(), before * 2.5)
        self.assertFalse(herb.getGrimy())

    def testGetGrimy(self):
        pass

    def testSetGrimy(self):
        pass


class TestCatalyst(unittest.TestCase):
    def testRefine(self):
        catalyst = Catalyst('Test Catalyst', 7, 7)
        catalyst.refine()
        self.assertEqual(catalyst.getQuality(), 8.1)
        catalyst.refine()
        self.assertEqual(catalyst.getQuality(), 9.2)
        catalyst.refine()
        self.assertEqual(catalyst.getQuality(), 10.0)

    def testGetQuality(self):
        pass


unittest.main()
