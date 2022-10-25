from crypt import methods
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import dojo 



#CREATE

@app.route('/create/dojo', methods=["POST"])
def create_dojo():
    dojo.Dojo.create_dojo(request.form)
    return redirect('/dojo')


#READ

@app.route('/')
def hp():
    return render_template('dojo.html')

@app.route('/dojo')
def dojo_info():
    all_dojos = dojo.Dojo.get_all()
    print(all_dojos)
    return render_template('dojo.html', all_dojos = all_dojos)

@app.route('/dojo/show/<int:id>')
def get_dojo_with_ninjas(id):
    data = {
            "id" : id
    }
    get_dojo_with_ninjas = dojo.Dojo.get_dojo_with_ninjas(data)
    return render_template('dojo_show.html', dojo = get_dojo_with_ninjas )






# #UPDATE




# #DELETE

# @app.route('/users/delete/<int:id>')
# def delete_user(id):
#     ninja.User.delete_users_by_id(id)
#     return redirect('/')