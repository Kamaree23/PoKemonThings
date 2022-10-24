from App import app
from flask import render_template, redirect, url_for, request
from .Catchem import catchEmAll
from .forms import CatchEmAll
import requests as r 

@app.route('/')
def home():

    return render_template('index.html')

@app.route('/PoKemonSearch', methods=["POST", "GET"])
def searchPoKemon():
    form = CatchEmAll()
    
    if request.method == "POST":
       
        if form.validate():
           
            pokemon = form.pokemon.data
            pokedex = catchEmAll(pokemon)
            print(pokedex)     
            if isinstance(pokedex, (str)):
                print(pokedex)
                return pokedex
            else:
                return render_template('Selected.html', pokedex=pokedex)
         
    return render_template('Search_Pokemon.html', form = form)

@app.route('/SelectedPokemon', methods=["GET", "POST"])
def selectedPokemon():
   return render_template('selected.html')
