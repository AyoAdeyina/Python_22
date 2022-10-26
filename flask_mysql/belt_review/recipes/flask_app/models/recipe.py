from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask_app import app
from flask_app.models import user
from flask import flash, session
import re
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

class Recipe:
    db = "meal_recipes"

    def __init__(self, data):
        self.name = data['name']
        self.description = data['description']
        self.instruction = data['instruction']
        self.date = data['date']
        self.under_30_minutes = data['under_30_minutes']
        self.create_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data ['user_id']
        self.id = data['id']


#CREATE-SQL

    @classmethod
    def create_recipe(cls,data):
        if not cls.validate_recipe_data(data):
            return False
        query = """
        INSERT INTO recipes(name, description, instruction, date, under_30_minutes, user_id)
        VALUES (%(name)s, %(description)s, %(instruction)s, %(date)s, %(under_30_minutes)s, %(user_id)s)
        ;"""
        recipe_id = connectToMySQL(cls.db).query_db(query, data)
        print('Created user with id of', recipe_id)
        
        return recipe_id





#READ-SQL

    @classmethod
    def get_all_recipes(cls):
        query = """
        SELECT *
        FROM recipes
        ;"""
        result = connectToMySQL(cls.db).query_db(query)
        recipes = []
        print('***********', result)

        for recipe_info in result:
            recipes.append(cls(recipe_info))
        return recipes

    @classmethod
    def get_recipe_by_id(cls, id):
        data = { 'id' : id}
        query = """
        SELECT *
        FROM recipes 
        WHERE id = %(id)s;"""
        result = connectToMySQL(cls.db).query_db(query, data)
        if result:
            result = cls(result[0])
        return result





#UPDATE-SQL
    @classmethod
    # def update_recipe_by_id(cls,id):
    #     data = { 'id' : id }
    #     query = """
    #     UPDATE recipes 
    #     SET name = %(name)s, description = %(description)s, instruction = %(instruction)s, 
    #     date = %(date)s, under_30_minutes = %(under_30_minutes)s, updated_at = NOW() 
    #     WHERE id = %(id)s;"""
    #     return connectToMySQL(cls.db).query_db(query, data)

    def update_recipe_by_id(cls,data):
        if not cls.validate_recipe_data(data):
            return False
        query = """
        UPDATE recipes 
        SET name = %(name)s, description = %(description)s, instruction = %(instruction)s, 
        date = %(date)s, under_30_minutes = %(under_30_minutes)s, updated_at = NOW() 
        WHERE id = %(id)s;"""
        result = connectToMySQL(cls.db).query_db(query, data)
        return True


#DELETE-SQL

    @classmethod
    def destroy_recipe_by_id(cls,id):
        data = {'id' : id}
        query = """
        DELETE FROM recipes 
        WHERE id = %(id)s;"""
        return connectToMySQL(cls.db).query_db(query, data)

#VALIDATE-SQL

    @staticmethod
    def validate_recipe_data(data):
        is_valid = True
        if len(data['name']) < 3:
            flash('Your name must be at least three characters long!')
            is_valid = False
        if len(data['description']) < 3:
            flash('Your description must be at least three characters long!')
            is_valid = False
        if len(data['instruction']) < 3:
            flash('Your instruction must be three characters long!')
            is_valid = False
        return is_valid