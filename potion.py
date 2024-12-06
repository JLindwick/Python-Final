from item import Item

class pokemonFaintError(Exception):
    def __init__(self):
        print(f"Pokemon is fainted, can't heal")

class Potion(Item):
    def __init__(self, name, quantity):
        super().__init__(name, quantity)

    def getQuantity(self):
        return self.quantity
    
    def setQuantity(self,value):
        self.setQuantity = value

    def healPokemon(self,pokemon):
        pokemonMaxHp = pokemon.getMaxHealth()
        pokemonCurrentHp = pokemon.getCurrentHealth()
        try:
            if pokemonCurrentHp <=0:
                raise pokemonFaintError
            else:
                if pokemonCurrentHp == pokemonMaxHp:
                    print(f"Pokemon at Full Health, the potion was not used")
                else:
                    if (pokemonCurrentHp + 20) > pokemonMaxHp:
                        self.quantity -= 1
                        pokemon.setCurrentHealth(pokemon.getMaxHealth())
                        print(f"You healed {pokemon.name} to full hp")
                    else:
                        self.quantity -= 1
                        pokemon.setCurrentHealth(pokemonCurrentHp + 20)
                        print(f"You used a potion, {pokemon.name} was healed 20 HP and is at {pokemon.getCurrentHealth()}")
        except pokemonFaintError as e:
            print(e)
            return
        
def __str__(self):
    return f"Name: {self.name} type: {self.quantity}"