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
    def testGetAttack(self):
        alchemist = Alchemist(1, 2, 3, 4, 5, 6, None)
        self.assertEqual(alchemist.getAttack(), 1)
    
    def testGetStrength(self):
        alchemist = Alchemist(1, 2, 3, 4, 5, 6, None)
        self.assertEqual(alchemist.getStrength(), 2)

    def testGetDefence(self):
        alchemist = Alchemist(1, 2, 3, 4, 5, 6, None)
        self.assertEqual(alchemist.getDefence(), 3)
    
    def testGetMagic(self):
        alchemist = Alchemist(1, 2, 3, 4, 5, 6, None)
        self.assertEqual(alchemist.getMagic(), 4)
    
    def testGetRanged(self):
        alchemist = Alchemist(1, 2, 3, 4, 5, 6, None)
        self.assertEqual(alchemist.getRanged(), 5)
    
    def testGetNecromancy(self):
        alchemist = Alchemist(1, 2, 3, 4, 5, 6, None)
        self.assertEqual(alchemist.getNecromancy(), 6)

    def testGetLaboratory(self):
        lab = Laboratory([], [], [])
        alchemist = Alchemist(1, 1, 1, 1, 1, 1, lab)
        self.assertEqual(alchemist.getLaboratory(), lab)

    def testGetRecipies(self):
        lab = Laboratory([], [], [])
        alchemist = Alchemist(1, 1, 1, 1, 1, 1, lab)
        self.assertEqual(alchemist.getRecipies(), {
            "Super Attack": ["Irit", "Eye of Newt"],
            "Super Strength": ["Kwuarm", "Limpwurt Root"],
            "Super Defence": ["Cadantine", "White Berries"],
            "Super Magic": ["Lantadyme", "Potato Cactus"],
            "Super Ranging": ["Dwarf Weed", "Wine of Zamorak"],
            "Super Necromancy": ["Arbuck", "Blood of Orcus"],
            "Extreme Attack": ["Avantoe", "Super Attack"],
            "Extreme Strength": ["Dwarf Weed", "Super Strength"],
            "Extreme Defence": ["Lantadyme", "Super Defence"],
            "Extreme Magic": ["Ground Mud Rune", "Super Magic"],
            "Extreme Ranging": ["Grenwall Spike", "Super Ranging"],
            "Extreme Necromancy": ["Ground Miasma Rune", "Super Necromancy"]})

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
        for recipe in alchemist.getRecipies():
            alchemist.mixPotion(recipe) 

        self.assertEqual(len(alchemist.getLaboratory().getPotions()), 6)


    def testDrinkPotion(self):
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
        for recipe in alchemist.getRecipies():
            alchemist.mixPotion(recipe) 

        for potion in alchemist.getLaboratory().getPotions():
            print(alchemist.drinkPotion(potion))

        self.assertEqual(alchemist.getAttack(), 68.05)
        self.assertEqual(alchemist.getStrength(), 78.85)
        self.assertEqual(alchemist.getDefence(), 31.599999999999998)
        self.assertEqual(alchemist.getMagic(), 20.4985)
        self.assertEqual(alchemist.getRanged(), 289.225)
        self.assertEqual(alchemist.getNecromancy(), 173.75500000000002)

    def testCollectReagent(self):
        lab = Laboratory([], [], [])
        alchemist = Alchemist(1, 1, 1, 1, 1, 1, lab)
        herb = Herb("test", 10)
        catalyst = Catalyst("Dog", 7, 5)
        alchemist.collectReagent(herb, 1)
        self.assertEqual(len(lab.getHerbs()), 1)
        alchemist.collectReagent(catalyst, 1)
        self.assertEqual(len(lab.getCatalysts()), 1)

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
        herb = Herb("test", 10)
        catalyst = Catalyst("Dog", 7, 5)
        potion = SuperPotion(herb, catalyst, "Name", "Stat", 1.0)
        self.assertEqual(potion.getName(), "Name")

    def testGetStat(self):
        herb = Herb("test", 10)
        catalyst = Catalyst("Dog", 7, 5)
        potion = SuperPotion(herb, catalyst, "Name", "Stat", 1.0)
        self.assertEqual(potion.getStat(), "Stat")

    def testGetBoost(self):
        herb = Herb("test", 10)
        catalyst = Catalyst("Dog", 7, 5)
        potion = SuperPotion(herb, catalyst, "Name", "Stat", 1.0)
        self.assertEqual(potion.getBoost(), 1.0)

    def testSetBoost(self):
        herb = Herb("test", 10)
        catalyst = Catalyst("Dog", 7, 5)
        potion = SuperPotion(herb, catalyst, "Name", "Stat", 1.0)
        potion.setBoost(10)
        self.assertEqual(potion.getBoost(), 10)


class TestSuperPotion(unittest.TestCase):
    def testCalculateBoost(self):
        herb = Herb("test", 10)
        catalyst = Catalyst("Dog", 7, 5)
        superPotion = SuperPotion(herb, catalyst, "testPotion", "stat", -1.0)
        self.assertEqual(superPotion.calculateBoost(), (10 + (7*5)*1.5))
        
    def testGetHerb(self):
        herb = Herb("test", 10)
        catalyst = Catalyst("Dog", 7, 5)
        superPotion = SuperPotion(herb, catalyst, "testPotion", "stat", -1.0)
        self.assertEqual(superPotion.getHerb(), herb)

    def testGetCatalyst(self):
        herb = Herb("test", 10)
        catalyst = Catalyst("Dog", 7, 5)
        superPotion = SuperPotion(herb, catalyst, "testPotion", "stat", -1.0)
        self.assertEqual(superPotion.getCatalyst(), catalyst)


class TestExtremePotion(unittest.TestCase):
    def testCalculateBoost(self):
        herb = Herb("test", 10)
        catalyst = Catalyst("Dog", 7, 5)
        superPotion = SuperPotion(herb, catalyst, "testPotion", "stat", -1.0)
        extremePotion = ExtremePotion(catalyst, superPotion, "Test", False, 1)
        self.assertEqual(extremePotion.calculateBoost(), 21.0)

    def testGetReagent(self):
        herb = Herb("test", 10)
        catalyst = Catalyst("Dog", 7, 5)
        superPotion = SuperPotion(herb, catalyst, "testPotion", "stat", -1.0)
        extremePotion = ExtremePotion(catalyst, superPotion, "Test", False, 1)
        self.assertEqual(extremePotion.getReagent(), catalyst)

    def testGetPotion(self):
        herb = Herb("test", 10)
        catalyst = Catalyst("Dog", 7, 5)
        superPotion = SuperPotion(herb, catalyst, "testPotion", "stat", -1.0)
        extremePotion = ExtremePotion(catalyst, superPotion, "Test", False, 1)
        self.assertEqual(extremePotion.getPotion(), superPotion)


class TestReagent(unittest.TestCase):
    def testGetName(self):
        herb = Herb("test", 10)
        self.assertEqual(herb.getName(), "test")

    def testGetPotency(self):
        herb = Herb("test", 10)
        self.assertEqual(herb.getPotency(), 10)

    def testSetPotency(self):
        herb = Herb("test", 10)
        herb.setPotency(15)
        self.assertEqual(herb.getPotency(), 15)


class TestHerb(unittest.TestCase):
    def testRefine(self):
        herb = Herb("test", 10)
        before = herb.getPotency()
        herb.refine()
        self.assertEqual(herb.getPotency(), before * 2.5)
        self.assertFalse(herb.getGrimy())

    def testGetGrimy(self):
        herb = Herb("test", 10)
        self.assertTrue(herb.getGrimy())

    def testSetGrimy(self):
        herb = Herb("test", 10)
        herb.setGrimy(False)
        self.assertFalse(herb.getGrimy())


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
        catalyst = Catalyst('Test Catalyst', 7, 14)
        self.assertEqual(catalyst.getQuality(), 14)


unittest.main()
