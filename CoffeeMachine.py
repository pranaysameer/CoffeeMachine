from python_json_config import ConfigBuilder
import json


class CoffeeMachine:

    """
    Is a Coffee Machine Class capable of handling multiple customers simultaneously.
    Keeps track of ingredients, supports reloading ingredients.
    """

    slots = 0                       # variable to contain number of beverages that can be filled simultaneously
    coffeeMachine = None            # variable to contain CoffeeMachine config
    ingredients = None              # variable to contain the ingredients quantities
    config = None                   # input json file
    beverages = None                # dictionary for holding requirements for each of the beverages
    availability = None             # variable that stores an array of timestamps showing till when a slot is reserved

    def __init__(self):
        """
        On initialization of Coffee Machine class the config is loaded and updates the class variables
        """
        self.config = ConfigBuilder().parse_config("coffeeMachineConfig.json")
        self.coffeeMachine = self.config.machine
        self.slots = self.coffeeMachine.outlets.count_n
        self.ingredients = json.loads(self.coffeeMachine.total_items_quantity.to_json())
        self.beverages = self.coffeeMachine.beverages
        self.availability = [0 for x in range(self.slots)]

    def getAvailability(self, timestamp: int) -> int:
        """
        Returns index of available slot
        Function takes in timestamp of when beverage making is being started and, checks if slot is available
        """
        for index, slot in enumerate(self.availability):
            if slot <= timestamp:
                return index
        print("No slot available, please wait..")
        return -1

    def bookSlot(self, index : int, timestamp: int):
        """
        Function takes in a timestamp, and an available slot and reserves it for the next 150s
        """
        self.availability[index] = timestamp + 150

    def fetchIngredients(self,requirement, drinkName : str):
        """
        Function takes in ingredients required to make a beverage and its name. If it can be prepared it goes ahead and prepares it.
        If any ingredient is insufficient or unavailable it notifies the user.
        """
        flag = all(key in self.ingredients.keys() and val <= self.ingredients[key] for key, val in requirement.items())
        if flag:
            for key, val in requirement.items():
                self.ingredients[key] -= val
            print(drinkName+" is prepared")
        else:
            unavailable = []
            insufficient = []
            for key, val in requirement.items():
                if key not in self.ingredients.keys():
                    unavailable.append(key)
                elif val > self.ingredients[key]:
                    insufficient.append(key)
            op = drinkName + " cannot be prepared because "
            op += ", ".join(unavailable) + " is not available. " if len(unavailable) > 0 else ""
            op += ", ".join(insufficient) + " is not sufficient" if len(insufficient) > 0 else ""
            print(op)

    def makeBeverage(self, drinkName : str, timestamp : int):
        """
        Takes in a drink name and tries to make it.
        First checks if slot is available.
        If available it checks for ingredients and if all present makes the ingredient and reserves the slot.
        """
        slot = self.getAvailability(timestamp)
        if slot != -1:
            beverage = json.loads(self.beverages.to_json())
            self.fetchIngredients(beverage[drinkName], drinkName)
            self.bookSlot(slot, timestamp)

    def refillIngredients(self, ingredient="hot_water", quantity=0, reloadConfig=False):
        """
        Function can be used to fill in ingredients.
        Option1: Loads a single ingredient using ingredient and quantity
        Option2: Load ingredients via dictionary ingredient.
        Option3: Load ingredients by reloading the configuration.
        """
        if reloadConfig:
            configPartial = ConfigBuilder().parse_config("coffeeMachineConfig.json")
            self.ingredients = json.loads(configPartial.machine.total_items_quantity.to_json())
            return
        if type(ingredient) == dict:
            for key, val in ingredient.items():
                self.ingredients[key] += val
        self.ingredients[ingredient] = quantity







