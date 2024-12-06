import random
from moves import Moves
import apiRequest
from collections import defaultdict
class Pokemon:
    pokemonChoice = []
    def __init__(self,name,pokeType,level,maxHealth,currentHealth,attack,defense,specialAttack,specialDefense,speed,moves):

        self.name = name
        self.pokeType = pokeType
        self.level = level
        self.maxHealth = maxHealth
        self.currentHealth = currentHealth
        self.attack = attack
        self.defense = defense
        self.specialAttack = specialAttack
        self.specialDefense = specialDefense
        self.speed = speed
        self.moves = moves
        Pokemon.pokemonChoice.append(self)

    def moveList(self):
        moveList = []
        for i in self.moves:
            moveList.append(Moves(i,self.moves[i],self.attack))
        return moveList

    def checkDamageMultiplier(self,move,defPokemonType):
        elementalCheckList = apiRequest.getTypesAdvantages()
        for i in range(len(defPokemonType.pokeType)):
            if defPokemonType.pokeType[i] in elementalCheckList[self.moves[move]]["strength"] :
                return 2
            elif defPokemonType.pokeType[i] in elementalCheckList[self.moves[move]]["weakness"] :
                return .5
        return .1
        
    def attackPokemon(self,attackUsed,defendingPokemon):
        damageMultiplier = self.checkDamageMultiplier(attackUsed,defendingPokemon)
        match damageMultiplier:
            case 2:
                print("Its super effective!")
            case .5:
                print("Its not that effective...")
        baseDamage = (random.randint(1,50) + self.attack) - defendingPokemon.defense
        attackDamage = baseDamage * damageMultiplier
        defendingPokemon.setCurrentHealth(defendingPokemon.currentHealth - max(attackDamage,0))
        print(f"{self.name} has {self.currentHealth} hp left and {defendingPokemon.name} has {defendingPokemon.currentHealth} hp left")
        
    def getName(self):
        return self.name

    def setName(self, value):
        self.name = value

    def getPokeType(self):
        return self.pokeType

    def setPokeType(self, value):
        self.pokeType = value

    def setCurrentHealth(self,value):
        self.currentHealth = value
    
    def getCurrentHealth(self):
        return self.currentHealth

    def getMaxHealth(self):
        return self.maxHealth

    def setMaxHealth(self, value):
        self.health = value
    
    def getAttack(self,value):
        self.attack = value

    def setAttack(self,value):
        self.attack = value

    def getDefense(self):
        return self.defense

    def setDefense(self, value):
        self.defense = value

    def getMoves(self):
        return self.moves

    def setMoves(self, value):
        self.moves = value

    def __str__(self):
        return f"Name: {self.name} type: {self.pokeType} max hp: {self.maxHealth} current hp: {self.currentHealth} attack: {self.attack} defense: {self.defense} moves: {self.moves}"