from unittest import result
from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask_app import app
from flask_app.models import ninja

class Dojo:
    db = "dojos_and_ninjas_schema"

    def __init__(self,data):
        self.name= data['name']
        self.create_at = data['created_at']
        self.updated_at = data['updated_at']
        self.id = data['id']
        self.ninjas = []

#CREATE

    @classmethod
    def create_dojo(cls,data):
        query = """
        INSERT INTO dojos (name)
        VALUES (%(name)s)
        ;"""
        result = connectToMySQL(cls.db).query_db(query, data)
        return result




#READ

    @classmethod
    def get_all(cls):
        query = """
        SELECT *
        FROM dojos
        ;"""
        result = connectToMySQL(cls.db).query_db(query)
        dojos = []
        print('***********', result)

        for dojo_info in result:
            dojos.append(cls(dojo_info))
        return dojos

    @classmethod
    def get_dojo_with_ninjas(cls, data):
        query = """
        SELECT * 
        FROM dojos
        LEFT JOIN ninjas on ninjas.dojo_id = dojos.id
        WHERE dojos.id = %(id)s
        ;"""
        result = connectToMySQL(cls.db).query_db(query, data)
        dojo = cls( result[0] )

        for dojo_ninja_info in result:
            ninja_data = {
                'first_name' : dojo_ninja_info['first_name'],
                'last_name' : dojo_ninja_info['last_name'],
                'age' : dojo_ninja_info['age'],
                'created_at' : dojo_ninja_info['ninjas.created_at'],
                'updated_at' : dojo_ninja_info['ninjas.updated_at'],
                'dojo_id' : dojo_ninja_info['dojo_id'],
                'id' : dojo_ninja_info['ninjas.id']
            }
            dojo.ninjas.append(ninja.Ninja(ninja_data))
        return dojo


#UPDATE




#DELETE



