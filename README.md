
# Pokémon Battle Simulator

## Overview

The **Pokémon Battle Simulator** is a turn-based game that allows players to build their Pokémon team, battle opponents, and experience Pokémon-style gameplay. The program integrates with the **Pokémon API** to dynamically fetch Pokémon stats, moves, sounds, and type advantages, ensuring an authentic experience.

The game also provides modular code, making it easy to extend and add new mechanics.

---

## Features

- **Dynamic API Integration**:
  - Fetch real-time Pokémon stats, moves, and type advantages using the Pokémon API.
  - Hear Pokémon cry sounds retrieved from the API during battles.
- **Team Building**:
  - Choose your Pokémon team (up to 6 Pokémon) from any generation or a mix of all generations.
- **Wild Pokémon Encounters**:
  - Battle and attempt to catch wild Pokémon using Pokéballs.
- **Trainer Battles**:
  - Battle against AI-controlled teams randomly generated from your chosen generation.
- **Turn-Based Combat**:
  - Battle system includes type advantages, moves, and Pokémon stats like attack, defense, and speed.
- **Item System**:
  - Use Potions to heal or Pokéballs to capture Pokémon during wild encounters.

---

## Prerequisites

- **Python 3.8+**
- **Dependencies**:
  - `requests` (for API calls)
  - Modules:
    - `pokemon.py`: Manages Pokémon properties and moves.
    - `team.py`: Handles team management.
    - `pokeball.py`: Implements capturing mechanics.
    - `potion.py`: Manages healing mechanics.
    - `apiRequest.py`: Fetches data from the Pokémon API.

---

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```bash
   cd pokemon-battle-simulator
   ```
3. Install required dependencies:
   ```bash
   pip install requests
   ```

---

## API Integration

The **Pokémon API** (https://pokeapi.co/) is used extensively to enhance gameplay. Here's how the API contributes to the simulator:

- **Fetching Generations**:
  - The program retrieves the list of all available Pokémon generations (e.g., Gen I, Gen II, etc.).
- **Getting Pokémon Stats**:
  - For each Pokémon selected or encountered, the API provides stats like HP, attack, defense, speed, and type.
- **Moves and Sounds**:
  - The API fetches a randomized list of four moves per Pokémon and plays their cries during battle.
- **Type Advantages**:
  - Dynamically fetches type interactions to calculate battle damage modifiers (e.g., water vs. fire).

> **Note**: An internet connection is required for API functionality. If the API is unavailable, the game may not load Pokémon data.

---

## How to Play

### Running the Game
1. Launch the program:
   ```bash
   python main.py
   ```

2. **Select a Pokémon Generation**:
   - Choose a generation to define the pool of Pokémon available for your team and opponents.

3. **Build Your Team**:
   - Pick up to six Pokémon from the selected generation. If you’re unsure, type `done` to end team selection early.

4. **Engage in Battles**:
   - Choose between wild encounters or trainer battles.
   - Use items, switch Pokémon, or execute moves strategically during combat.

---

## Gameplay Instructions

### **Main Menu**
1. **Wild Encounters**:
   - Battle or catch wild Pokémon using your Pokéballs.
2. **Trainer Battles**:
   - Compete against AI trainers with randomized Pokémon teams.

### **Battle Options**
- **Fight**: Use one of your Pokémon's moves.
- **Switch Pokémon**: Change your active Pokémon.
- **Use Items**: Heal with potions or use Pokéballs (wild battles only).
- **Run**: Escape from a wild encounter or forfeit a trainer battle.

---

## Example Gameplay

1. **Choose a Pokémon Generation**:
   ```
   1. All
   2. Generation 1
   ...
   10. Generation 9
   Which generation would you like to use?: 1
   ```

2. **Build Your Team**:
   ```
   Please enter the name of the Pokémon you want on your team:
   pikachu
   bulbasaur
   done
   ```

3. **Battle Example**:
   - Your team: Pikachu, Bulbasaur.
   - Opponent's Pokémon: Charmander.

   ```
   Pikachu's moves:
   1. Thunderbolt    2. Quick Attack
   3. Iron Tail      4. Electro Ball
   Which move would you like to use?: 1
   Pikachu used Thunderbolt!
   It's super effective!
   ```

---

## Key Functions

- **API Calls**:
  - `getGenerations()`: Retrieves all Pokémon generations.
  - `getGenerationPokemon()`: Fetches Pokémon names for a given generation.
  - `getPokemonStats()`: Retrieves detailed stats for a specific Pokémon.
  - `getTypesAdvantages()`: Fetches and calculates type effectiveness.
  - `getPokemonMove()`: Gets a pool of available moves for a Pokémon.
  - `pickRandomFourMoves()`: Randomly selects four moves from the pool.
  - `getPokemonSound()`: Plays the cry sound of a Pokémon.

- **Game Functions**:
  - `choosePokemonTeam()`: Allows players to build their team.
  - `chooseOpponentPokemonTeam()`: Randomly generates an AI opponent's team.
  - `battle()`: Manages turn-based combat between teams.

---

## Future Improvements

- Add leveling, experience points, and evolution mechanics.
- Introduce status effects like paralysis, poison, and sleep.
- Enhance AI with strategic behavior based on type matchups.
- Enable persistent game saves.
- Add multiplayer functionality for player-vs-player battles.

---

## Contributing

If you’re interested in improving the game, feel free to fork the repository, make changes, and submit a pull request. Suggestions are always welcome!
