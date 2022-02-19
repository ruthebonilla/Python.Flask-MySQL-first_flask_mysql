from flask_app.config.mysqlconnection import connectToMySQL 

class Friend:
    def __init__(self, data):
        self.id = data['id']
        
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def all_friends(cls):
        query = "SELECT * FROM friends;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('first_flask').query_db(query)
        # Create an empty list to append our instances of friends
        print(results)
        
        all_peeps = []
        # Iterate over the db results and create instances of friends with cls.
        for friend in results:
            all_peeps.append( cls(friend) )
            
        print(all_peeps)
        return all_peeps

    @classmethod
    def one_friend(cls, data):
        query = "SELECT * FROM friends WHERE id = %(id)s;"
        results = connectToMySQL('first_flask').query_db(query, data)
        return cls(results[0])

    @classmethod
    def save_friend(cls, data):
        query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(occupation)s, NOW(), NOW());"
        new_id = connectToMySQL("first_flask").query_db(query, data)
        return new_id
