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
            user = User(username, email, password, fname, lname)
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


@auth.route('/Profile/<username>')
def viewProfile(username):
    
    profile = User.query.filter_by(username=current_user.username).first()
    if username != current_user.username:
            flash('You cannot access this!')
            return redirect(url_for('auth.LogMeOut'))


    return render_template('viewProfile.html', profile=profile)


@auth.route('/Profile/edit/<username>',  methods=["GET", "POST"])
def editProfile(username):

    form = SignUp()

    profile = User.query.filter_by(username=current_user.username).first()
    print(form, profile)
    if request.method == "POST":
        print('POST')
        print(form.validate())
        print(form.errors)
        if form.validate():
            print('almost done')
            username = form.username.data
            fname = form.fname.data
            lname = form.lname.data
            email = form.email.data
            password = form.email.data
            confirm_password = form.confirm_password.data

            profile.username = username
            profile.fname = fname
            profile.lname = lname
            profile.email = email
            profile.password = password
            profile.confirm_password = confirm_password

            profile.updateToDB()

            print('finish')

        return redirect(url_for('auth.viewProfile',  username = current_user.username))




    return render_template('editProfile.html', form = form, profile = profile)


@auth.route('/logout')
def logMeOut():
    logout_user()
    return redirect(url_for('auth.login'))

