from unicodedata import name
import requests as r
def catchEmAll(pokemon):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    response = r.get(url)
    if response.ok:
        data = response.json()
        pokedex = {}
        stat = data
        pokedex = {
                'name': stat['name'],
                'bhp': stat['stats'][0]['base_stat'],
                'bdf': stat['stats'][2]['base_stat'],
                'batk': stat['stats'][1]['base_stat'],
                'img': stat['sprites']['other']['official-artwork']['front_default'],
                'ability': stat['abilities'][0]['ability']['name'],
                'weight': stat['weight']
            }
        return pokedex
    return "Error - that's not a Pokemon"


