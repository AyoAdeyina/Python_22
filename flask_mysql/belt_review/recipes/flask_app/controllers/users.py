from crypt import methods
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import user, recipe


#CREATE

@app.route('/users/register', methods = ["POST"])
def register_users():
    if user.User.create_user(request.form):
        return redirect('/users/profile')
    return redirect ('/')


#READ

@app.route('/')
def home():
    return render_template('registration.html')

@app.route('/users/profile')
def profile():
    all_recipes = recipe.Recipe.get_all_recipes()
    this_user = user.User.get_user_by_id(session['user_id'])
    return render_template('profile.html', this_user = this_user, all_recipes = all_recipes)

@app.route('/users/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/users/login', methods= ['POST'])
def login_user():
    if user.User.login(request.form):
        return redirect('/users/profile')
    return redirect('/')



#UPDATE




#DELETE

