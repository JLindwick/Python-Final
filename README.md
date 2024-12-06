**Pokémon Battle Utility Library**
This Python project provides a comprehensive set of tools and functionalities to interact with the Pokémon API (pokeapi.co) and perform various operations like fetching Pokémon data, generating type advantages, and building dynamic Pokémon movesets.

**Features**
Roman Numerals Conversion
Convert Roman numerals into integers for usability in Pokémon generation naming.

**API Connectivity**
Retrieves detailed Pokémon data from the Pokémon API, including:

**Pokémon regions**
Pokémon types and their strengths/weaknesses
Generations and associated Pokémon
Pokémon stats, moves, and type-specific advantages
Dynamic Pokémon Battle System

**Assigns random moves to Pokémon.**
Includes type effectiveness (strengths and weaknesses) for more realistic battles.
Pokémon Sound Effects
Plays Pokémon cries using vlc.

**Installation**

**Prerequisites**
Python 3.8 or higher

**Dependencies**:
requests: For API communication
vlc: To play Pokémon cries
random: For random sampling of movesets
Install the required dependencies via pip:
pip install requests python-vlc

**Usage**
Roman Numerals Conversion:
Convert Roman numerals to integers for tasks like identifying Pokémon generations.
Example:

roman_to_int("iv")  # Returns 4
Fetch Pokémon Regions
Retrieve a list of all Pokémon regions from the API:

regions = getRegions()
print(regions)  # ['kanto', 'johto', ...]
Get Pokémon Types and Their Advantages
Retrieve Pokémon types, their strengths, and weaknesses:

type_advantages = getTypesAdvantages()
print(type_advantages['fire'])  
**{'strength': ['grass', 'bug', 'ice', 'steel'], 'weakness': ['water', 'rock', 'ground']}**
Fetch Pokémon Stats
Retrieve stats for a specific Pokémon:

stats = getPokemonStats("pikachu")
print(stats)  
**{'speed': 90, 'special-defense': 50, 'special-attack': 50, 'defense': 40, 'attack': 55, 'hp': 35, 'type': ['electric']}**
Generate a Moveset for a Pokémon
Randomly assign four moves to a Pokémon:

moves = getPokemonMove("charizard")
random_moves = pickRandomFourMoves(moves)
print(random_moves)
**{'flamethrower': 'fire', 'fly': 'flying', ...}**
Play Pokémon Cries
Play a Pokémon’s cry sound:

getPokemonSound(pikachu)
Error Handling
This library includes robust error handling:

apiConnectionError: Raised when there’s an issue connecting to the Pokémon API.
Invalid API responses are gracefully handled with appropriate error messages.
Code Overview
Functions
General Utilities
romanToInt(s): Converts a Roman numeral string to an integer.
checkResponse(response): Ensures API responses are valid and returns JSON data.
Pokémon API Interactions
getRegions(): Fetches a list of all Pokémon regions.
getPokemonTypes(): Fetches a list of all Pokémon types.
getTypesAdvantages(): Builds a dictionary of type strengths and weaknesses.
getGenerations(): Fetches Pokémon generations and converts their Roman numeral names to integers.
getGenerationPokemon(generation): Fetches all Pokémon from a specific generation.
getPokemonStats(pokemon): Fetches a Pokémon's stats and types.
getPokemonMove(pokemon): Retrieves a list of all moves available to a Pokémon.
pickRandomFourMoves(movesList): Randomly selects four moves and fetches their types.
Audio
getPokemonSound(pokemon): Plays a Pokémon’s cry.
Future Enhancements
Add a Pokémon battle simulation using the type advantages and stats.
Implement caching for API calls to reduce latency and API usage.
Expand support for more Pokémon features, such as abilities and evolutions.
License
This project is licensed under the MIT License. See the LICENSE file for more details.
