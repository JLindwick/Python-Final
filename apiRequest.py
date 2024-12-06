import random
import requests
import sys
import vlc

#------------------------------------------------------------------------------#
#---------------[Roman Numerals Explanation]-----------------------------------#
#-------------------[Roman Numeral Values]-------------------------------------#
#--------[I-1, V-5, X-10, L-50, C-100, D-500, M-1000]--------------------------#
#--------------------------[Rules]---------------------------------------------#
#-----[1)If a symbol is placed after another of equal or greater value]--------# 
#--------then those values are added together]---------------------------------#
#-----[2)To represent numbers without a corresponding letter such as a---------#
#--------four, letters are placed before one of greater value so as to subtract#
#--------its value. IV would be equal to the larger number subtracted by-------# 
#--------the larger number so in this case 5(V)-1(I)=4]------------------------#
#------------------------------------------------------------------------------#

class apiConnectionError(Exception):
    def __init__(self):
        print(f"Network connection interrupted, please run the program again.")
        sys.exit()

#I could have installed and used roman, but I had written the algo for roman numerals a while ago so I just copy pasted it in and commented it up lol
def romanToInt(s):
    romanValues = {'i': 1, 'v': 5, 'x': 10, 'l': 50, 'c': 100, 'd': 500, 'm': 1000}
    result = 0
    prevValue = 0
    for numeral in reversed(s): #Loop through value in reverse its easier to identify if I need to subtract the value or not this way
        currentValue = romanValues[numeral] #set the current value equal to first digit in value
        if currentValue < prevValue: #if this value is less than the previous value subtract from the result so using VII
            result -= currentValue   #we now have IIV and our previous value is 0 and our current value is I or 1 so in the first iteration of the loop 1 is added to the result
        else:                        #In the second iteration of the loop its another I or 1 so 1 is not less than our previous value we add it to result which is now 2
            result += currentValue   #In the third iteration of the loop our current value is V or 5 which is still not less than our previous value so it gets added to the 
        prevValue = currentValue     #result adding up to 7. If our number was IX the value would be reversed to XI current value would start at 10, and the next iteration
    return result                    #1 our current value is less than our previous value of 10 so we subtract one so our result is 9

#make sure the data is saved otherwise raise exception
def checkResponse(response):
    try:
        if response.status_code != 204 and response.headers["content-type"].strip().startswith("application/json"):
            data = response.json() 
        else:
            raise apiConnectionError
    except apiConnectionError as e:
        print(e)
    return data

def getPokemonSound(pokemon):
    pokedexUrl = f"https://pokeapi.co/api/v2/pokemon/{pokemon.name}"
    response = requests.get(pokedexUrl)
    data = checkResponse(response)
    pokeCryLink = data['cries']['latest']
    mediaPlayerInstance = vlc.Instance()
    mediaPlayer = mediaPlayerInstance.media_player_new()
    media = mediaPlayerInstance.media_new(pokeCryLink)
    mediaPlayer.set_media(media)
    mediaPlayer.play()
    while mediaPlayer.is_playing():
        pass

def getRegions():
    regionsUrl = "https://pokeapi.co/api/v2/region/" #this url responds with data that holds all region data in pokemon.
    regionsList = [] #holds empty region list
    response = requests.get(regionsUrl) #response value becomes the data the url returns
    data = checkResponse(response)
    for region in data['results']: #search through the data looking at the key results
        regionsList.append(region['name']) #add the region's name to the list
    return regionsList #return that list

def getPokemonTypes():
    typesUrl = "https://pokeapi.co/api/v2/type/" #this url responds with data that holds all the pokemon types.
    typesList = []
    response = requests.get(typesUrl)
    data = checkResponse(response)
    for type in data['results']:
        typesList.append(type['name'])
    return typesList

# This is where things get spicy lmao the way I had my original pokemon game working I hardcoded the types, with their weakness and strengths of those moves
# for example I had a dictionary elementalTypesList = {"fire":{"strength":"grass","weakness":"water"} I had to update this because in actuality pokemon can have multiple types
# So I needed to see if the moves type was super effective against or not very effective against any of the pokemon types 
# 'fighting': {'strength': ['normal', 'rock', 'steel', 'ice', 'dark'], 'weakness': ['flying', 'psychic', 'fairy']} here is an example output from the created list
# So If the move was fighting and the pokemon's type was normal, rock, steel, ice, or dark it would return super effective (2x damage) if the type of the pokemon was in the
# weakness category it would return not very effective (.5 damage)


def getTypesAdvantages():
    pokemonTypes = getPokemonTypes()
    strengthAndWeaknessList = {}
    for i in range(len(pokemonTypes)-1):
        typeAdvantageUrl = f"https://pokeapi.co/api/v2/type/{i+1}" #this url responds with data that holds all the advantages a type has over other types
        weakness = [] #list to hold weakness
        strengths = [] #list to hold strengths
        response = requests.get(typeAdvantageUrl) #get response data
        data = checkResponse(response) #convert to json
        for j in range(len(data["damage_relations"]['double_damage_from'])): #going into the data I look at the values for key "damage_relations" and within that the values for the key "double_damage_from"
            weakness.append(data["damage_relations"]['double_damage_from'][j]["name"]) #append the weaknesses for this type in the weakness list
        for k in range(len(data["damage_relations"]['double_damage_to'])): #looking at the same key "damage_relations" I then look at the values within another key "double_damage_to"
            strengths.append(data["damage_relations"]['double_damage_to'][k]["name"]) #append the strength to the list
        strengthAndWeaknessList[pokemonTypes[i]] = {"strength":strengths,"weakness":weakness} #then return the list in a way that I can work with so "fighting":{"strengths":[all strengths],"weakness":[all weakness]}
    return strengthAndWeaknessList

def getGenerations():
    generationUrl = 'https://pokeapi.co/api/v2/generation/' #this url responds with data that holds all the generation data within pokemon
    generationList = []
    generationListNoRoman = []
    response = requests.get(generationUrl)
    data = checkResponse(response)
    for generation in data['results']:
        generationList.append(generation['name'])
    for i in range(len(generationList)): #pokemon api creators for some reason used roman numerals to list their games, I wanted the game generation to correspond to a number choice
        convertRomanValue = str(generationList[i]).replace("generation-","") #original printout of the results is "generation-vi" so to work with just the roman numeral "generation-" was cut from string
        convertedNumber = romanToInt(convertRomanValue) #convert to roman numeral
        finalizedString = f"Generation {convertedNumber}" #add "Generation" string plus the value of the roman numeral
        generationListNoRoman.append(finalizedString) #append that generation to the list
    return generationListNoRoman

def getGenerationPokemon(generation):
    pokedexUrl = f"https://pokeapi.co/api/v2/pokedex/{generation}" #this url responds with data that gives all the pokemon within a certain generation or all of the generations depending on selection
    pokemonList = []
    response = requests.get(pokedexUrl)
    data = checkResponse(response)
    for i in range(len(data['pokemon_entries'])):
        pokemonList.append(data['pokemon_entries'][i]['pokemon_species']['name'])
    return pokemonList

def getPokemonStats(pokemon):
    pokemonURL = f"https://pokeapi.co/api/v2/pokemon/{pokemon}" #this url responds with data that gathers an individual pokemon's stats
    response = requests.get(pokemonURL)
    pokeStats = {}
    data = checkResponse(response)
    for stat in data['stats']:
        pokeStats[stat['stat']['name']] = stat['base_stat']
    types = []
    for type in data['types']:
        types.append(type['type']['name'])
    pokeStats['type'] = types
    return pokeStats

def getPokemonMove(pokemon):
    pokemonURL = f"https://pokeapi.co/api/v2/pokemon/{pokemon}" #this url responds with data that holds all of an individual pokemon's moves
    response = requests.get(pokemonURL)
    moveList = []
    data = checkResponse(response)
    for moves in data["moves"]:
        moveList.append(moves['move']['name'])
    return moveList

def pickRandomFourMoves(movesList):
    randomMoves = random.sample(movesList, 4)
    moveDict = {}
    for i in range(len(randomMoves)):
        pokemonURL = f"https://pokeapi.co/api/v2/move/{randomMoves[i]}" #this url responds with data about a specific move and its stats
        response = requests.get(pokemonURL)
        data = checkResponse(response)
        moveDict[data['name']] = data['type']['name']
    return moveDict
