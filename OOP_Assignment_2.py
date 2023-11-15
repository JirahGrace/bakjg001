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
    ''' A class to represent the potion attributes and methods.
        
        Attributes
        ------------
        name: str
            name of the potion
        stat: str
            the stat of the potion (super/extreme)
        boost: float
            the boost which the potion provides.

        Methods
        ------------
        caculateBoost():
            Abstract function for caculating the boost amount of the potion
        getName (): str
            Returns the name of the potion
        getStat (): str
            Returns the stat of the potion
        getBoost(): float
            Returns the boost of the potion
        setBoost(boost: float):
            Sets the potion boost amount. 
    '''
    def __init__(self, name:str, stat:str, boost:float):
        self.__name = name
        self.__stat = stat
        self.__boost = boost

    
    @abstractmethod
    def calculateBoost(self):
        ''' Abstract Method blueprint for caculating the boost amount of the potion, function raises an error if directly called'''
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
    ''' A class to represent the reagent attributes and methods.
        
        Attributes
        ------------
        name: str
            name of the potion
        potency: float
            the potency of the ingredient
    
        Methods
        ------------
        refine ():
            abstract method blueprint for refining the ingredients
        getName (): str
            Returns the name of the ingredient
        getPotency(): float
            Returns the potency of the ingredient
        setPotency(boost: float):
            Sets the potency of the ingredient 
    '''
    def __init__(self, name:str, potency:float):
        self.__name = name
        self.__potency = potency

    @abstractmethod
    def refine(self):
        ''' Abstract Method blueprint for refining ingrediens, function raises an error if directly called'''
        raise Exception("Abstract Method Called")

    def getName(self):
        return self.__name

    def getPotency(self):
        return self.__potency

    def setPotency(self, potency):
        self.__potency = potency


class Herb(Reagent):
    ''' A class which inherits from Reagent to represent the herb ingredient
        
        Attributes
        ------------
        grimy = True
    
        Methods
        ------------
        refine (): str
            refines the herb by multiplying by 2.5
        getGrimy (): bool
            Returns whether or not the herb is grimy
        setGrimy(grimy: bool):
            Sets the the state of grimy of the herb 
    '''
    def __init__(self, name:str, potency:float):
        super().__init__(name, potency)
        self.__grimy = True

    def refine(self):
        '''Function refines the herb by multiply the potency by 2.5 if it has not already been refined'''
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
    ''' A class which inherits from Reagent to represent the catalyst ingredient
        
        Attributes
        ------------
        quality: float
    
        Methods
        ------------
        refine (): str
            refines the catalyst by adding quality of 1.1, up to a quality of 10
        getQuality (): float
            Returns the quality of the catalyst.
    '''
    def __init__(self, name:str, potency:float, quality:float):
        super().__init__(name, potency)
        self.__quality = quality

    def refine(self):
        ''' Functions refines the catalyst by testing the current quality level, 
            if the level is less than 10 it can be refined by adding 1.1'''
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
    ''' A class to represent the super potion attributes and methods.
        
        Attributes
        ------------
        herb: Herb
            type of herb ingredient
        catalyst: Catalyst
            type of catalyst ingredient
        
        Methods
        ------------
        caculateBoost():
            Function for caculating the boost of the super potion
        getHerb (): Herb
            Returns the herb ingredient used in the potion
        getCatalyst (): Catalyst
            Returns the catalyst ingredient used in the potion
    '''
    def __init__(self, herb:Herb, catalyst:Catalyst, name, stat, boost):
        super().__init__(name, stat, boost)
        self.__herb = herb
        self.__catalyst = catalyst

    def calculateBoost(self) -> float:
        ''' Function caculates the boost amount of the super potion, 
            uses the formuala potency of its herb + (potency of its catalyst * quality of its catalyst) * 1.5'''
        boost = self.getHerb().getPotency() + (self.getCatalyst().getPotency() * self.getCatalyst().getQuality()) * 1.5
        return boost

    def getHerb(self):
        return self.__herb

    def getCatalyst(self):
        return self.__catalyst


class ExtremePotion(Potion):
    ''' A class to represent the extreme potion attributes and methods.
        
        Attributes
        ------------
        reagent: Reagent
            Reagent ingredient in the recipe
        potion: Potion
            Super potion ingredient
        
        Methods
        ------------
        caculateBoost():
            Function for caculating the boost of the super potion
        getReagent (): Reagent
            Returns the reagent ingredient used in the potion
        getPotion (): Potion
            Returns the super potion ingredient used in the potion
    '''
    def __init__(self, reagent:Reagent, potion:Potion, name:str, stat:str, boost:float):
        super().__init__(name, stat, boost)
        self.__reagent = reagent
        self.__potion = potion

    def calculateBoost(self) -> float:
        ''' Function caculates the boost amount of the extreme potion, 
            uses the formuala (potency of its reagent * boost value of its super potion) * 3.0'''
        boost = (self.getReagent().getPotency() * self.getBoost()) * 3.0
        return boost

    def getReagent(self):
        return self.__reagent

    def getPotion(self):
        return self.__potion


class Laboratory:
    ''' A class to represent the laboratory attributes and methods.
        
        Attributes
        ------------
        potion: Potion[]
            List containing all the potions
        herb: Herb[]
            List containing all the herbs
        catalyst: Catalyst[]
            List containing all the catalysts
        
        Methods
        ------------
        mixPotion(name:str, type:str, stat:str, primaryIngredient:str, secondaryIngredient:str):
            Function which collects ingridents and mixes potions according the the recipes.
        addReagent (reagent:Reagent, amount: int): 
            Adds a reagent to the respective lists of ingredients (either herb or catalyst)
    '''
    def __init__(self, potions:[Potion], herbs:[Herb], catalysts:[Catalyst]):
        self.__potions = potions
        self.__herbs = herbs
        self.__catalysts = catalysts

    def getHerbs(self) -> [Herb]:
        return self.__herbs
    
    def getCatalysts(self) -> [Catalyst]:
        return self.__catalysts
    
    def getPotions(self) -> [Potion]:
        return self.__potions
    
    def mixPotion(self, name:str, type:str, stat:str, primaryIngredient:str, secondaryIngredient:str):
        ''' Function takes in the name, ingredients and details of the potions and creates a potion to add to super potion 
            or extreme potion and removes the used ingredients from their respective lists'''
        firstIngredient = None
        secondIngredient = None
        for herb in self.getHerbs():
            if herb.getName() == primaryIngredient:
                firstIngredient = herb
                self.getHerbs().remove(herb)
                break
        for catalyst in self.getCatalysts():
            if catalyst.getName() == primaryIngredient:
                firstIngredient = catalyst
                self.getCatalysts().remove(catalyst)
                break
            if catalyst.getName() == secondaryIngredient:
                secondIngredient = catalyst
                self.getCatalysts().remove(catalyst)
                break
        if secondIngredient is not None:
            self.__potions.append(SuperPotion(firstIngredient, secondIngredient, name, stat, 1))
            return 
        for potion in self.__potions:
            if potion.getName() == secondaryIngredient:
                secondIngredient = potion
                self.__potions.remove(potion)
                break
        if secondIngredient is not None:
            self.__potions.append(ExtremePotion(firstIngredient, secondaryIngredient, name, stat, secondIngredient.calculateBoost()))
            return
                                  
    def addReagent(self, reagent:Reagent, amount:int):
        ''' Takes the imput of a herb or catalyst and the amount and adds the amount of that reagent to its appropriate list'''
        if isinstance(reagent, Herb):
            self.__herbs.extend([reagent]*amount)
        elif isinstance(reagent, Catalyst):
            self.__catalysts.extend([reagent]*amount)
        else:
            raise Exception("Unknown Reagent Type")


class Alchemist:
    ''' A class to represent the alchemist attributes and methods.
        
        Attributes
        ------------
        attack: int
            Attack power
        strength: int
            Alchemist's strength
        defense: int
            Alchemist's defence power
        magic: int
            Number representing the Alchemist's magic ability
        ranged: int
            Ranged attack power
        necromancy: int
            Necromancy ability
        laboratory: Laboratory 
            Iteration of the laboratory class which contains the Alchemist's potions
        recipes: {}
            Dictionary containing all the potion recipes

        Methods
        ------------
        getLaboratory(): Laboratory
            Returns an iteration of the laboratory
        getRecipe(): {}
            Returns a recipe from the dictionary
        mixPotion(recipe: str):
            Function which collects ingridents and mixes potions according the the recipes.
        drinkPotion(potion: Potion): str
            Function which allows the Alchemist to 'consume' potions and increases the appropriate stats
        collectReagents(reagent: Reagent, amount: int):
            Function takes a reagent type and the amount and adds it to the respective lists
        refineReagents():
            Function refines all reagents
    '''
    def __init__(self, attack:int, strength:int, defense:int, magic:int, ranged:int, necromancy:int, laboratory:Laboratory):
        self.__attack = attack
        self.__strength = strength 
        self.__defense = defense
        self.__magic = magic
        self.__ranged = ranged
        self.__necromancy = necromancy
        self.__laboratory = laboratory
        self.__recipes = {
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
            "Extreme Necromancy": ["Ground Miasma Rune", "Super Necromancy"]}
        
    def getAttack(self):
        return self.__attack
    
    def getStrength(self):
        return self.__strength
    
    def getDefence(self):
        return self.__defense
    
    def getMagic(self):
        return self.__magic
    
    def getRanged(self):
        return self.__ranged
    
    def getNecromancy(self):
        return self.__necromancy

    def getLaboratory(self):
        return self.__laboratory

    def getRecipies(self):
        return self.__recipes

    def mixPotion(self, recipe):
        if recipe not in self.__recipes:
            return
        
        type, stat = recipe.split(" ")

        [firstIngredient, secondIngredient] = self.__recipes[recipe]
        self.__laboratory.mixPotion(recipe, type, stat, firstIngredient, secondIngredient)

    def drinkPotion(self, potion:Potion):
        ''' Function allows Alchemist to 'drink' the potion, takes a potion as an input and increases 
            the appropriate stat, function displays corresponsing messages to the screen'''
        output = "Drinking " + potion.getName()
        if potion.getStat() == "Attack":
            self.__attack += potion.calculateBoost()
            output = output + ": Attack increased to " + str(self.__attack)
        elif potion.getStat() == "Strength":
            self.__strength += potion.calculateBoost()
            output = output + ": Strength increased to " + str(self.__strength)
        elif potion.getStat() == "Defence":
            self.__defense += potion.calculateBoost()
            output = output + ": Defence increased to " + str(self.__defense)
        elif potion.getStat() == "Magic":
            self.__magic += potion.calculateBoost()
            output = output + ": Magic increased to " + str(self.__magic)
        elif potion.getStat() == "Ranging":
            self.__ranged += potion.calculateBoost()
            output = output + ": Ranging increased to " + str(self.__ranged)
        elif potion.getStat() == "Necromancy":
            self.__necromancy += potion.calculateBoost()
            output = output + ": Necromancy increased to " + str(self.__necromancy)
        else:
            raise Exception(f'Unknown stat {potion.getStat()}')
        return output

    def collectReagent(self, reagent, amount):
        ''' Function takes in a reagent and amount as parameters and appends the appropriate lists to include the new amount of reagents'''
        self.__laboratory.addReagent(reagent, amount)

    def refineReagents(self):
        ''' Function refines all reagents in the herb and catalyst lists using the refine methods in Herb and Catalyst'''
        for herb in self.getLaboratory().getHerbs():
            herb.refine()

        for catalyst in self.getLaboratory().getCatalysts():
            catalyst.refine()