from flask import Flask, jsonify, request

app = Flask(__name__)

pokemons = [
    {"name": "Pikachu", "type": "Elétrico"},
    {"name": "Charmander", "type": "Fogo"},
    {"name": "Bulbasaur", "type": "Grama/Veneno"},
]

MAX_PAGINATION_LIMIT = 5

# rota de metodo GET para listar os pokemons
@app.route("/lista", methods=["GET"])
def list_pokemons():
    offset = int(request.args.get("offset", 0))
    limit = int(request.args.get("limit", MAX_PAGINATION_LIMIT))

    if limit > MAX_PAGINATION_LIMIT:
        limit = MAX_PAGINATION_LIMIT

    return jsonify(pokemons[offset:offset + limit])

# rota para buscar um pokemon pelo nome
@app.route("/<pokemon_name>", methods=["GET"])
def find_pokemon(pokemon_name):
    for pokemon in pokemons:
        if pokemon["name"].lower() == pokemon_name:
            return jsonify(pokemon)
    return jsonify({"error" : "pokemon not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)