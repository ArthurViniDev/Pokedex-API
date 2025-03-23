class Pokemon:
    pokemons = [
        {"name": "Pikachu", "type": "Electric"},
        {"name": "Charmander", "type": "Fire"},
        {"name": "Bulbasaur", "type": "Grass/Poison"},
        {"name": "Eevee", "type": "Grass"},
        {"name": "Squirtle", "type": "Water"},
        {"name": "Jigglypuff", "type": "Normal/Fairy"},
        {"name": "Meowth", "type": "Normal"},
        {"name": "Psyduck", "type": "Water"},
        {"name": "Snorlax", "type": "Normal"},
        {"name": "Gengar", "type": "Ghost/Poison"}
    ]

    @classmethod
    def list_pokemons(cls, offset=0, limit=5):
        return cls.pokemons[offset:offset + limit]

    @classmethod
    def find_pokemon(cls, name):
        for pokemon in cls.pokemons:
            if pokemon["name"].lower() == name.lower():
                return pokemon
        return None

    @classmethod
    def add_pokemon(cls, new_pokemon):
        if not new_pokemon or "name" not in new_pokemon or "type" not in new_pokemon:
            return None
        cls.pokemons.append(new_pokemon)
        return new_pokemon
