from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']

    @classmethod
    def add(cls,data):
        print("here")
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        return cls(results[0])

    @classmethod
    def all_ninjas(cls):
        query = "SELECT * FROM ninjas;"
        ninjas_from_db= connectToMySQL('dojos_and_ninjas').query_db(query)
        all_ninjas = []
        for ninja in ninjas_from_db:
            all_ninjas.append(cls(ninja))
            return all_ninjas

