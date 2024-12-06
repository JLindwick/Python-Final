from item import Item
import sys
class notEnoughPokeballs(Exception):
    def __init__(self, quantity):
        super().__init__(quantity)
        self.quantity = quantity
        print(f"You have {quantity} Pokeballs!")

class cannotCatchPokemon(Exception):
    def __init__(self):
        print("Attempt failed, cannot catch pokemon. You lose one pokeball.")

class Pokeball(Item):
    def __init__(self, name, quantity):
        super().__init__(name, quantity)

    def getQuantity(self):
        return self.quantity
    
    def setQuantity(self,value):
        self.setQuantity = value

    def catchPokemon(self,pokemon,playerTeam):
        try:
            if self.quantity <1:
                raise notEnoughPokeballs
            else:
                percentageCatchHp = pokemon.getMaxHealth() * (40/100)
                try:
                    if pokemon.getCurrentHealth() <= percentageCatchHp:
                        self.quantity -= 1
                        playerTeam.addPokemon(pokemon)
                        print(f"You caught {pokemon.name}")
                    else:
                        self.quantity -= 1
                        raise cannotCatchPokemon
                except cannotCatchPokemon as e:
                    print(e)
        except notEnoughPokeballs as e:
            print(e)
def __str__(self):
    return f"Name: {self.name} type: {self.quantity}"