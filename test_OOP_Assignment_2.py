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
        pass

    def testDrinkPotion(self):
        pass

    def testCollectReagent(self):
        pass

    def testRefineReagent(self):
        herb = Herb("test", 10)
        catalyst = Catalyst("Dog", 7, 5)
        alchemist = Alchemist(0, 0, 0, 0, 0, 0, Laboratory([], [], []))
        alchemist.collectReagents(herb, 1)
        alchemist.collectReagents(catalyst, 1)
        alchemist.refineReagents()
        self.assertEqual(alchemist.getLaboratory().getHerbs()[0].getPotency(), 25.0)
        self.assertEqual(alchemist.getLaboratory().getCatalysts()[0].getQuality(), 6.1)


class TestLaboratory(unittest.TestCase):
    def testMixPotion(self):
        pass

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
