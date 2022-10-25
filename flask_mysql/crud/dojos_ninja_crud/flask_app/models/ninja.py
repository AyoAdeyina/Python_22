from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask_app import app

class Ninja:
    
    db = "dojos_and_ninjas_schema"

    def __init__(self, data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']
        self.id = data['id']


#CREATE
    @classmethod
    def create_ninja(cls,data):
        query = """
        INSERT INTO ninjas (first_name, last_name, age, dojo_id)
        VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s)
        ;"""
        return connectToMySQL(cls.db).query_db(query, data)




#READ

    @classmethod
    def get_all_ninjas(cls):
        query = """
        SELECT *
        FROM ninjas
        ;"""
        result = connectToMySQL(cls.db).query_db(query)
        ninjas = []
        print('***********', result)

        for ninja_info in result:
            ninjas.append(cls(ninja_info))
        return ninjas



# #UPDATE




# #DELETE
