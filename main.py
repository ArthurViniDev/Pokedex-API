from flask import Flask
from routes.pokemon import pokemon_routes

app = Flask(__name__)
app.register_blueprint(pokemon_routes)

if __name__ == "__main__":
    app.run(debug=True)