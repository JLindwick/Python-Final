import random
import sys
from pokemon import Pokemon
from team import Team
from pokeball import Pokeball
from potion import Potion
import apiRequest
import time

generations = apiRequest.getGenerations()
types = apiRequest.getPokemonTypes()
for i in range(len(generations)):
    if i+1 == 1:
        print(f"{i+1}. All")
    else:
        print(f"{i+1}. {generations[i-1]}")
        
generationChoice = input("Which generation would you like to use?: ")

if int(generationChoice) <= len(generations):
    pokemonChoiceList = apiRequest.getGenerationPokemon(int(generationChoice))
    apiRequest.getTypesAdvantages()
else:
    print("invalid generation, please run program again")
    sys.exit()
#Starting Items
playerPotion = Potion("potion",5)
playerPokeball = Pokeball("pokeball",5)

class pokemonFaintedError(Exception):
    def __init__(self):
        print(f"Pokemon has fainted, cannot select this pokemon.")
       
def choosePokemonTeam():
    pokemonTeam = []
    print("Please enter the name of the pokemon you want on your team from the following list (maximum of 6, entering done will end pokemon selection early)")  
    print(' '.join(pokemonChoiceList))
    for i in range(6):
        while True:
            pokemonChoice = input(f"pokemon slot {i+1}: ").lower()
            if pokemonChoice == "done":
                if len(pokemonTeam) >0:
                    team = Team(pokemonTeam,0)
                    return team
                else:
                    print("no pokemon selected, please retry later")
                    sys.exit()
            else: 
                try:
                    if pokemonChoice in pokemonChoiceList:
                        pokemonStats = apiRequest.getPokemonStats(pokemonChoice)
                        pokemonTeam.append(Pokemon(pokemonChoice,pokemonStats['type'],1,pokemonStats['hp'],pokemonStats['hp'],pokemonStats['attack'],pokemonStats['defense'],pokemonStats['special-attack'],pokemonStats['special-defense'],pokemonStats['speed'],apiRequest.pickRandomFourMoves(apiRequest.getPokemonMove(pokemonChoice))))
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("Invalid choice, please choose again or enter done if you are done selecting.")                           
    team = Team(pokemonTeam,0)
    return team

def chooseOpponentPokemonTeam():
    randomPokemon = random.sample(range(0,len(pokemonChoiceList)),6)
    opponentTeam = []
    for i in range(len(randomPokemon)):
        pokemonStats = apiRequest.getPokemonStats(randomPokemon[i])
        opponentTeam.append(Pokemon(pokemonChoiceList[randomPokemon[i]],pokemonStats['type'],1,pokemonStats['hp'],pokemonStats['hp'],pokemonStats['attack'],pokemonStats['defense'],pokemonStats['special-attack'],pokemonStats['special-defense'],pokemonStats['speed'],apiRequest.pickRandomFourMoves(apiRequest.getPokemonMove(randomPokemon[i]))))
    team = Team(opponentTeam,0)
    return team

# User Battle choices
def mainBattle(myTeam, opponentTeam):
    print("Your team: ")
    for i in range(len(myTeam.pokemonTeam)):
        print(myTeam.pokemonTeam[i].name,end="\t")
    print("\n1. Catch more pokemon")
    print("2. Battle a pokemon trainer?")
    playerChoice = input("Choose 1 or 2: ")
    if not playerChoice.isdigit():
        print("invalid choice please enter a number")
        mainBattle(myTeam,opponentTeam)
    elif int(playerChoice) <1 or int(playerChoice)>2:
        print("invalid selection, please choose 1 or 2")
        mainBattle(myTeam, opponentTeam)
    else:
        if int(playerChoice) == 1:
            while myTeam.checkPartyFainted() == False:
                battle(myTeam,opponentTeam,"randomEncounter",True,True)
        elif int(playerChoice) == 2:
            print("Opponents team: ")
            for i in range(len(opponentTeam.pokemonTeam)):
                print(opponentTeam.pokemonTeam[i].name)
            while opponentTeam.checkPartyFainted() == False:
                battle(myTeam,opponentTeam,"trainerEncounter",True,True)

def getPlayerMove(pokemon):
    print(f"{pokemon.name}'s moves:")
    for i, move in enumerate(pokemon.moves):
        if(i+1 == 3):
            print("\n")
        print(f"{i+1}. {move}", end="\t")
    print("\n")
    choice = input("Which move would you like to use?: ")
    if int(choice) > 0 and int(choice) < 5:
        for i, move in enumerate(pokemon.moves):
            if int(choice) == i+1:
                return move
    else:
        print("Invalid Selection. Please type the move from the above list. ")
        getPlayerMove(pokemon)
                
def getEnemyAttack(opponent,randomNumber):
    for i,opponentMove in enumerate(opponent.moves):
        if i == randomNumber:
            return opponentMove

def changeEnemyPokemon(team):
    for i in range(len(team.pokemonTeam)):
        if i != team.active:
            if team.pokemonTeam[i].getCurrentHealth() > 0:
                team.changeActivePokemon(i)
                break
    
def changeMyPokemon(team):
    currentPokemon = team.getActivePokemon()
    print(f"Current Pokemon: {currentPokemon.name}")
    if len(team.pokemonTeam) < 2:
        print("Cannot change pokemon")
    else:
        for i in range(len(team.pokemonTeam)):
            if team.active != i:
                print(f"{i+1}. {team.pokemonTeam[i].name} \t")
        change = input("Select by choosing the number next to the pokemon: ")
        if change.isdigit():
            for i in range(len(team.pokemonTeam)):
                try:
                    if team.pokemonTeam[int(change)-1].getCurrentHealth() > 0:
                        team.changeActivePokemon(int(change)-1)
                    else:
                        raise pokemonFaintedError
                except pokemonFaintedError as e:
                    print(e)
        else:
            print("Please choose a numerical value.")
    print(f"Active Pokemon: {team.getActivePokemon()}")


def battleMenu():
    print("Please choose action from the following list: ")
    print("1. FIGHT\t 2. PKMN\n")
    print("3. ITEMS\t 4. RUN\n")
    choice = input("Please enter a number between 1 and 4 for your selection: ")
    return choice

def itemMenu(team,opponentTeam,battleType):
    if battleType == "randomEncounter":
        print(f"What would you like to use? 1. Potion {playerPotion.quantity} 2. Pokeball {playerPokeball.quantity}")
        choice = input("Please select with 1 or 2: ")
        if int(choice) == 1:
            potionMenu(team)
        elif int(choice) == 2:
            playerPokeball.catchPokemon(opponentTeam.pokemonTeam[opponentTeam.active],team)
            battle(team,opponentTeam,"randomEncounter",False,False)
    elif battleType == "trainerEncounter":
        potionMenu(team)

def potionMenu(team):
    potionQuantity = playerPotion.checkQuantity()
    if potionQuantity == True:
        for i in range(len(team.pokemonTeam)):
            print(f"{i+1}. {team.pokemonTeam[i]}")
        choice = input("Which pokemon would you like to use a potion on?: ")
        playerPotion.healPokemon(team.pokemonTeam[int(choice)-1])
    else:
        print("Out of potions!")    

def battle(myTeam, opponentTeam, typeOfBattle,playMyTeam,playMyOpponentTeam):
    activePokemon = myTeam.getActivePokemon()
    activeOpponentPokemon = opponentTeam.getActivePokemon()
    if playMyTeam == True:
        print("You bring out:")
    print(activePokemon)
    if playMyTeam == True:
        apiRequest.getPokemonSound(activePokemon)
    time.sleep(1.25)
    print("Your opponent is: ")
    print(activeOpponentPokemon)
    if playMyOpponentTeam == True:
        apiRequest.getPokemonSound(activeOpponentPokemon)
    while activePokemon.getCurrentHealth() > 0 and activeOpponentPokemon.getCurrentHealth() >0:
        action = battleMenu()
        match int(action):
            case 1:
                if typeOfBattle == "randomEncounter":
                    myPokemonMove = getPlayerMove(activePokemon)
                    print(f"{activePokemon.name} used: {myPokemonMove}")
                    activePokemon.attackPokemon(myPokemonMove,activeOpponentPokemon)
                    if activeOpponentPokemon.getCurrentHealth() <= 0:
                        if playMyOpponentTeam == True:
                            apiRequest.getPokemonSound(activeOpponentPokemon)
                        print(f"{activeOpponentPokemon.name} has been defeated.")
                        sys.exit()
                    randomAttack = random.randint(0,3)
                    opponentPokemonAttack = getEnemyAttack(activeOpponentPokemon,randomAttack)
                    print(opponentPokemonAttack)
                    print(f"{activeOpponentPokemon.name} used: {opponentPokemonAttack}")
                    activeOpponentPokemon.attackPokemon(opponentPokemonAttack,activePokemon)
                    if activePokemon.getCurrentHealth() <=0:
                        if playMyTeam == True:
                            apiRequest.getPokemonSound(activePokemon)
                        if myTeam.checkPartyFainted() == False:
                            print("Pokemon fainted, please choose another!")
                            changeMyPokemon(myTeam)
                            if playMyTeam == True:
                                apiRequest.getPokemonSound(activePokemon)
                            print(myTeam.active)
                            continue
                        else:
                            print(f"Your last pokemon {activePokemon.name} fainted, returning to a Pokemon Center")
                            sys.exit()
                elif typeOfBattle == "trainerEncounter":
                    myPokemonMove = getPlayerMove(activePokemon)
                    print(f"{activePokemon.name} used: {myPokemonMove}")
                    activePokemon.attackPokemon(myPokemonMove,activeOpponentPokemon)
                    randomAttack = random.randint(0,3)
                    opponentPokemonAttack = getEnemyAttack(activeOpponentPokemon,randomAttack)
                    print(f"{activeOpponentPokemon.name} used: {opponentPokemonAttack}")
                    activeOpponentPokemon.attackPokemon(opponentPokemonAttack,activePokemon)
                    if activePokemon.getCurrentHealth() <=0:
                        if myTeam.checkPartyFainted() == False:
                            print("Pokemon fainted, please choose another!")
                            changeMyPokemon(myTeam)
                            print(myTeam.active)
                            continue
                        elif myTeam.checkPartyFainted() == True:
                            print(f"You and {activePokemon.name} lost to {activeOpponentPokemon.name}")
                            sys.exit()
                    elif activeOpponentPokemon.getCurrentHealth() <=0:
                        if opponentTeam.checkPartyFainted() == False:
                            print("Opponent pokemon fainted, they are switching pokemon...")
                            changeEnemyPokemon(opponentTeam)
                            activeOpponentPokemon = opponentTeam.getActivePokemon()
                            print(f"Opponent has selected: {activeOpponentPokemon}")
                            apiRequest.getPokemonSound(activeOpponentPokemon)
                            continue
                        elif opponentTeam.checkPartyFainted() == True:
                            print(f"You and {activePokemon.name} won against {activeOpponentPokemon.name}")
                            break
                    elif activePokemon.getCurrentHealth() <=0 and activeOpponentPokemon.getCurrentHealth() <= 0:
                        if myTeam.checkPartyFainted() == False and opponentTeam.checkPartyFainted() == False:
                            print("Pokemon fainted, please choose another!")
                            changeMyPokemon(myTeam)
                            print(myTeam.getActivePokemon())
                            print("Opponent pokemon fainted, they are switching pokemon...")
                            changeEnemyPokemon(opponentTeam)
                            print(f"Opponent has selected: {opponentTeam.pokemonTeam[opponentTeam.active]}")
                            continue    
            case 2: 
                print("Choose another pokemon!")
                changeMyPokemon(myTeam)
                battle(myTeam,opponentTeam,typeOfBattle,True,False)
                continue
            case 3:
                itemMenu(myTeam,opponentTeam,typeOfBattle)
                continue
            case 4:
                if typeOfBattle == "randomEncounter":
                    print("You ran away")
                    sys.exit()
                elif typeOfBattle == "trainerEncounter":
                    print("You ran away and lost all your money!")
                    sys.exit()

if __name__ == "__main__":
    opponentTeam = chooseOpponentPokemonTeam()
    myTeam = choosePokemonTeam()
    mainBattle(myTeam,opponentTeam)