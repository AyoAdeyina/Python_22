from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import ninja, dojo


#CREATE

@app.route('/create/ninja', methods=['POST'])
def create_ninja():
    ninja.Ninja.create_ninja(request.form)
    return redirect (f"/dojo/show/{request.form['dojo_id']}")


#READ

@app.route('/')
def dojo_ninjas():
    all_ninjas = ninja.Ninja.get_all_ninjas()
    return render_template('dojo.html', all_ninjas = all_ninjas)

@app.route('/add_ninja')
def add_ninja():
    all_dojos = dojo.Dojo.get_all()
    return render_template('ninja.html', all_dojos = all_dojos)

# @app.route('/home')
# def home():
#     return render_template('dojo.html')

# #UPDATE

# @app.route('/users/update', methods = "POST")
# def update_users():
#     ninja.User.update_user(request.form)
#     return redirect('/')


# #DELETE

# @app.route('/users/delete/<int:id>')
# def delete_user(id):
#     ninja.User.delete_users_by_id(id)
#     return redirect('/')
