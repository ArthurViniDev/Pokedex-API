from flask import Flask, jsonify, request

app = Flask(__name__)

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

MAX_PAGINATION_LIMIT = 5

# Rota GET para listar os Pokémon
@app.route("/list", methods=["GET"])
def list_pokemons():
    offset = int(request.args.get("offset", 0))
    limit = int(request.args.get("limit", MAX_PAGINATION_LIMIT))
    if limit > MAX_PAGINATION_LIMIT:
        limit = MAX_PAGINATION_LIMIT
    return jsonify(pokemons[offset:offset + limit])

# Rota GET para buscar um Pokémon pelo nome
@app.route("/pokemon/<pokemon_name>", methods=["GET"])
def find_pokemon(pokemon_name):
    for pokemon in pokemons:
        if pokemon["name"].lower() == pokemon_name.lower():
            return jsonify(pokemon)
    return jsonify({"error": "Pokémon not found"}), 404

@app.route("/add", methods=["POST"])
def add_pokemon():
    new_pokemon = request.get_json()
    if not new_pokemon or "name" not in new_pokemon or "type" not in new_pokemon:
        return jsonify({"error": "Invalid Pokémon"}), 400
    pokemons.append(new_pokemon)
    return jsonify(new_pokemon), 201

if __name__ == "__main__":
    app.run(debug=True)
