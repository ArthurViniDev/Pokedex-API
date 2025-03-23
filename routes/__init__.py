from flask import Blueprint

# Criando um blueprint global, caso queira importar tudo de uma vez
routes = Blueprint("routes", __name__)
