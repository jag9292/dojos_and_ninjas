from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.ninjas = []


    @classmethod
    def all_dojos(cls):
        query = "SELECT * FROM dojos;"
        dojos_from_db= connectToMySQL('dojos_and_ninjas').query_db(query)
        all_dojos = []
        for dojo in dojos_from_db:
            all_dojos.append(cls(dojo))
        return all_dojos

    
    @classmethod
    def add_dojo(cls,data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        return connectToMySQL('dojos_and_ninjas').query_db(query,data)

    
    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        return cls(results[0])


    @classmethod
    def get_ninja_by_dojo(cls,data):
        query = "SELECT * FROM dojos JOIN ninjas ON dojos.id = dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query,data)

        group = cls(results[0])

        for row_from_db in results:
            data = {
                "id": row_from_db["ninjas.id"],
                "first_name": row_from_db["first_name"],
                "last_name": row_from_db["last_name"],
                "age": row_from_db["age"],
            }
            group.ninjas.append(Ninja(data))
        return group