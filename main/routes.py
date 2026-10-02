from flask import render_template
from . import main_bp

# id odpovídá číslu v Pokédexu (použije se pro obrázek z PokeAPI)
POKEMONS = [
    {"id": 25,  "name": "Pikachu",    "types": ["electric"]},
    {"id": 1,   "name": "Bulbasaur",  "types": ["grass", "poison"]},
    {"id": 4,   "name": "Charmander", "types": ["fire"]},
    {"id": 7,   "name": "Squirtle",   "types": ["water"]},
    {"id": 94,  "name": "Gengar",     "types": ["ghost", "poison"]},
    {"id": 133, "name": "Eevee",      "types": ["normal"]},
]


@main_bp.route("/")
def index():
    return render_template("main/index.html", pokemons=POKEMONS)


@main_bp.route("/about")
def about():
    return render_template("main/about.html")