from App import app
from flask import render_template, redirect, url_for, request
from .Catchem import catchEmAll
from .forms import CatchEmAll, Caught
from datetime import datetime


@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/PoKemonSearch', methods=["POST", "GET"])
def searchPoKemon():
    form = CatchEmAll()
    
    if request.method == "POST":
       
        if form.validate():
           
            pokemon = form.pokemon.data
            pokedex = catchEmAll(pokemon)


                
            if isinstance(pokedex, (str)):
                print(pokedex)
                return pokedex
            else:
                return render_template('Selected.html', pokedex=pokedex)
        
        
         
    return render_template('Search_Pokemon.html', form = form)



@app.route('/Selected', methods=["GET", "POST"])
def selectedPokemon():
    # form = Caught()
    # print(request.method)
    # if request.method == "POST":
    #     print(form.validate(), form.errors)
    #     if form.validate():
        #   print('valid')
        #   user_id = current_user.id
            # name = pokidex.name
            # date_created=datetime.utcnow()
    #         pokemon = Pokemon(user_id, name)
    #         pokemon.saveToDB()
    return render_template('selected.html')



# @app.route('/caught', methods=["GET", "POST"])
# @login_required
# def cacther():
#     pass




# @app.route('/MyTeam')
# @login_required
# def MyTeam(): 
#     pass