from flask import Blueprint, render_template, request, redirect, flash, url_for
from .forms import SignUp, Login
from App.models import User, db
from flask_login import login_user, logout_user, current_user
from werkzeug.security import check_password_hash



auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/signup', methods=["GET", "POST"])
def signUp():
    form = SignUp()
    if request.method == 'POST':
        print('POST')
        
        if form.validate():
            print('validated')
            username = form.username.data
            email = form.email.data
            fname = form.fname.data
            lname = form.lname.data
            password = form.password.data

            print(username, email, fname, lname, password)
            user = User(username, email, password)
            user.saveToDB()
        
        return redirect(url_for('auth.login'))

        
    
    return render_template('SignUp.html', form = form)

@auth.route('/login', methods=["GET", "POST"])
def login():
    form = Login()
    if request.method == "POST":
        if form.validate():
            username = form.username.data
            password = form.password.data
            print(username, password)

            user = User.query.filter_by(username=username).first()
            if user:
                if check_password_hash(user.password, password):
                    flash('succesfully logged in')
                    login_user(user)
                    return redirect(url_for('home'))
                else:
                   flash('Incorrect password')
            else:
                flash('User does not exist')
    return render_template('Login.html', form=form)



@auth.route('/logout')
def logMeOut():
    logout_user()
    return redirect(url_for('auth.login'))

