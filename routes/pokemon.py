from flask import Blueprint, jsonify, request
from models import Pokemon

pokemon_routes = Blueprint("pokemon_routes", __name__)

MAX_PAGINATION_LIMIT = 5

@pokemon_routes.route("/list", methods=["GET"])
def list_pokemons():
    offset = int(request.args.get("offset", 0))
    limit = int(request.args.get("limit", MAX_PAGINATION_LIMIT))
    limit = min(limit, MAX_PAGINATION_LIMIT)

    return jsonify(Pokemon.list_pokemons(offset, limit))

@pokemon_routes.route("/pokemon/<pokemon_name>", methods=["GET"])
def find_pokemon(pokemon_name):
    pokemon = Pokemon.find_pokemon(pokemon_name)
    if pokemon:
        return jsonify(pokemon)
    return jsonify({"error": "Pokémon not found"}), 404

@pokemon_routes.route("/add", methods=["POST"])
def add_pokemon():
    new_pokemon = request.get_json()
    added_pokemon = Pokemon.add_pokemon(new_pokemon)
    if added_pokemon:
        return jsonify(added_pokemon), 201
    return jsonify({"error": "Invalid Pokémon"}), 400