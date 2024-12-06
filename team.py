class Team:
    def __init__(self,pokemonTeam,active):
        self.pokemonTeam = pokemonTeam
        self.active = active

    def addPokemon(self,pokemon):
        self.pokemonTeam.append(pokemon)

    def removePokemon(self,pokemon):
        self.pokemonTeam.remove(pokemon)

    def getActivePokemon(self):
        for i in range(len(self.pokemonTeam)):
            if i == self.active:
                return self.pokemonTeam[i]
    
    def changeActivePokemon(self,active):
        self.active = active

    def checkPartyFainted(self):
        faintedCheck = []
        for i in self.pokemonTeam:
            if i.getCurrentHealth() <= 0:
                faintedCheck.append(True)
            else:
                faintedCheck.append(False)
        if all(faintedCheck):
            return True
        else:
            return False
        
    def __str__(self):
        pokemonTeam = [str(pokemon) for pokemon in self.pokemonTeam]
        joinPokemonTeam = "\n".join(pokemonTeam)
        activePokemon = self.getActivePokemon()
        return f"Team:\n{joinPokemonTeam}\n active pokemon: {activePokemon.name}"
