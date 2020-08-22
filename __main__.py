from CoffeeMachine import CoffeeMachine

def main():
    coffeeMachine = CoffeeMachine()
    coffeeMachine.makeBeverage("hot_tea",20)
    coffeeMachine.makeBeverage("hot_coffee",20)
    coffeeMachine.makeBeverage("green_tea",20)
    coffeeMachine.makeBeverage("black_tea",180)
    coffeeMachine.refillIngredients(reloadConfig=True)
    coffeeMachine.makeBeverage("hot_tea",200)
    coffeeMachine.makeBeverage("black_tea",280)
    coffeeMachine.makeBeverage("green_tea",450)
    coffeeMachine.makeBeverage("hot_coffee",500)
    coffeeMachine.refillIngredients(reloadConfig=True)
    coffeeMachine.makeBeverage("hot_coffee",550)
    coffeeMachine.makeBeverage("black_tea",600)
    coffeeMachine.makeBeverage("green_tea",600)
    coffeeMachine.makeBeverage("hot_tea",650)



if __name__ == "__main__":
    main()
