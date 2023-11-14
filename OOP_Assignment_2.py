'''
File: OOP Assignment 2.py
Description: Main Code File for RPG OOP Assignment 2.
Author: Jirah Baker
StudentID: 110332584
EmailID: bakjg001
This is my own work as defined by the University's Academic Misconduct Policy.
'''

from abc import ABC, abstractmethod

class Potion(ABC):
    '''A potion has a name, what kind of attribute of an alchemist it can increase (i.e., stat attribute), and by how
        much the attribute is increased (i.e., boost attribute).
        The boost is calculated differently depending on if it is a super potion or an extreme potion:
            • Super potion: potency of its herb + (potency of its catalyst * quality of its catalyst) * 1.5. The result
                should be rounded by 2 decimals.
            •  Extreme potion: (potency of its reagent * boost value of its super potion) * 3.0. The result should be
                rounded by two decimals.'''
    def __init__(self, name, stat, boost):
        self.__name = name
        self.__stat = stat
        self.__boost = boost

    @abstractmethod
    def calculateBoost(self):
        raise Exception("Abstract Method Called")

    def getName(self):
        return self.__name

    def getStat(self):
        return self.__stat

    def getBoost(self):
        return self.__boost

    def setBoost(self, boost):
        self.__boost = boost


class Reagent(ABC):
    ''' A reagent has a name and a potency value. A reagent can be refined but it depends on which type of
reagent it is and the refinement will result in something different.'''
    def __init__(self, name, potency):
        self.__name = name
        self.__potency = potency

    @abstractmethod
    def refine(self):
        pass

    def getName(self):
        return self.__name

    def getPotency(self):
        return self.__potency

    def setPotency(self, potency):
        self.__potency = potency


class Herb(Reagent):
    '''Herb: Refining leads to a herb that is not grimy and will multiply its existing potency by 2.5. It will
print this information on the screen as well.'''
    def __init__(self, grimy, name, potency):
        super().__init__(name, potency)
        self.__grimy = True

    def refine(self):
        if self.__grimy is True:
            self.setPotency(self.getPotency() * 2.5)
            print(f'{self.getName()} Refined: New Potency {self.getPotency()}')
        else:
            print(f'{self.getName()} cannot be refined any further.')
        self.setGrimy(False)

    def getGrimy(self):
        return self.__grimy

    def setGrimy(self, grimy):
        self.__grimy = grimy


class Catalyst(Reagent):
    ''' Catalyst: If the quality of the catalyst is below 8.9 then its quality will be increased by 1.1 and this
information is printed on the screen. If its quality is equal or above 8.9 then its quality is set to 10.
It should print on the screen the quality and say that “it cannot be refined any further”'''
    def __init__(self, quality, name, potency):
        super().__init__(name, potency)
        self.__quality = quality

    def refine(self):
        if self.__quality < 8.9:
            self.__quality = self.__quality + 1.1
            print(f'The quality of {self.getName()} has been increased by 1.1')
        elif self.__quality >= 8.9:
            self.__quality = 10
            print(f'The quality of {self.getName()} has been increased to 10 and cannnot be refined any further')
        else:
            print(f'{self.getName} cannot be refined any further.')


    def getQuality(self):
        return self.__quality

class SuperPotion(Potion):
    '''The boost is calculated differently depending on if it is a super potion or an extreme potion:
            • Super potion: potency of its herb + (potency of its catalyst * quality of its catalyst) * 1.5. The result
                should be rounded by 2 decimals.'''
    def __init__(self, herb:Herb, catalyst:Catalyst, name, stat, boost):
        super().__init__(name, stat, boost)
        self.__herb = herb
        self.__cataylst = catalyst

    def calculateBoost(self) -> float:
        boost = self.getHerb().getPotency() + (self.getCatalyst().getPotency() * self.getCatalyst().getQuality()) * 1.5
        return boost

    def getHerb(self):
        return self.__herb

    def getCatalyst(self):
        return self.__cataylst


class ExtremePotion(Potion):
    ''' Extreme potion: (potency of its reagent * boost value of its super potion) * 3.0. The result should be rounded by two decimals'''
    def __init__(self, reagent:Reagent, potion:Potion, name, stat, boost):
        super().__init__(name, stat, boost)
        self.__reagent = reagent
        self.__potion = potion

    def calculateBoost(self) -> float:
        boost = (self.getReagent().getPotency() * self.getBoost()) * 3.0
        return boost

    def getReagent(self):
        return self.__reagent

    def getPotion(self):
        return self.__potion


class Laboratory:
    ''' The laboratory stores the potions, herbs, and catalysts.
It provides functionality for an alchemist to mix potions: Each potion that is mixed has a name and its first
ingredient is either a herb or a catalyst that is stored in the laboratory. The second ingredient is either a
catalyst or another potion. Depending on the potion type, the proper potion must be created. Which
attribute of an alchemist the potion is increasing is specified in the status of the potions.
Reagents can be added to the laboratory. To keep it simple, this functionality specifies the amount of
reagents being available in the laboratory.'''
    def __init__(self, potions:list[Potion], herbs:list[Herb], catalysts:list[Catalyst]):
        self.__potions = potions
        self.__herbs = herbs
        self.__catalysts = catalysts

    def getHerbs(self):
        return self.__herbs
    
    def getCatalysts(self):
        return self.__catalysts
    
    def getPotions(self):
        return self.__potions
    
    def mixPotion(self, name:str, type:str, stat:str, primaryIngredient:str, secondaryIngredient:str):
        pass

    def addReagent(self, reagent:Reagent, amount:int):
        if isinstance(reagent, Herb):
            self.__herbs.extend([reagent]*amount)
        elif isinstance(reagent, Catalyst):
            self.__catalysts.extend([reagent]*amount)
        else:
            raise Exception("Unknown Reagent Type")


class Alchemist:
    ''' The attributes in Alchemist from attack to necromancy are values between 0 and 100 which indicate the
strength of that attribute. An alchemist knows the following recipes that can create two types of potions,
super potions and extreme potions. The recipe of a super potions consists of a herb and a catalyst. The
recipe of an extreme potion consists of a herb or catalyst and a super potion.'''
    def __init__(self, attack:int, strength:int, defense:int, magic:int, ranged:int, necromancy:int, laboratory:Laboratory):
        self.__attack = attack
        self.__strength = strength 
        self.__defense = defense
        self.__magic = magic
        self.__ranged = ranged
        self.__necromancy = necromancy
        self.__laboratory = laboratory
        self.__recipes = {}

    def getLaboratory(self):
        return self.__laboratory

    def getRecipies(self):
        return self.__recipes

    def mixPotion(self, recipe):
        pass

    def drinkPotion(self, potion):
        pass

    def collectReagents(self, reagent, amount):
        self.__laboratory.addReagent(reagent, amount)

    def refineReagents(self):
        for herb in self.getLaboratory().getHerbs():
            herb.refine()

        for catalyst in self.getLaboratory().getCatalysts():
            catalyst.refine()