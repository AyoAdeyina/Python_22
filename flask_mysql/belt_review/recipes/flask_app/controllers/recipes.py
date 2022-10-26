from crypt import methods
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import recipe, user


#CREATE-CONNECTION

@app.route('/recipes/create' , methods = ["POST", "GET"])
def create_recipe():
    if "user_id" in session:
        if request.method == "GET": 
            return render_template ('create_recipe.html')
        if recipe.Recipe.create_recipe(request.form):
            return redirect('/users/profile')
        else:
            return redirect ('/recipes/create')
    return redirect('/')
#READ-CONNECTION

@app.route('/recipes/show/<int:id>')
def show_recipe(id):
    show_recipe = recipe.Recipe.get_recipe_by_id(id)
    return render_template('view_recipe.html', show_recipe = show_recipe, this_user = user.User.get_user_by_id(session['user_id']))


#UPDATE-CONNECTION

@app.route('/recipes/edit/<int:id>')
def edit_recipe(id):
    if not "user_id" in session:
        return redirect('/')
    this_recipe = recipe.Recipe.get_recipe_by_id(id)
    return render_template('edit_recipe.html', this_recipe = this_recipe)

@app.route('/recipes/update', methods = ["POST"])
def update_recipe():
    # data = {
    #     'id' : request.form['id'],  #if id is not in request.form then this is needed to pass information into the update method!
    #     'name' : request.form['name'],
    #     'description' : request.form['description'],
    #     'instruction' : request.form['instruction'],
    #     'date' : request.form['date'],
    #     'under_30_minutes' : request.form['under_30_minutes']
    # }
    if recipe.Recipe.update_recipe_by_id(request.form):
        return redirect('/users/profile')
    else:
        return redirect(f'/recipes/edit/{request.form["id"]}')

#DELETE-CONNECTION

@app.route('/recipes/destroy/<int:id>')
def delete_recipe(id):
    if not "user_id" in session:
        return redirect('/')
    recipe.Recipe.destroy_recipe_by_id(id)
    return redirect('/users/profile')