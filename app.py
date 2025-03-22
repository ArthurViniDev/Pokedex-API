from flask import Flask, jsonify, request

app = Flask(__name__)

pokemons = [
    {"name": "Pikachu", "type": "Elétrico"},
    {"name": "Charmander", "type": "Fogo"},
    {"name": "Bulbasaur", "type": "Grama/Veneno"},
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

if __name__ == "__main__":
    app.run(debug=True)
