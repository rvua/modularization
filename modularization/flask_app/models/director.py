from flask_app.config.mysqlconnection import connectToMySQL
# from flask_app.controllers.directors import director
from flask_app.models.movie import Movie

class Director: 
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.year_born = data['year_born']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at'] 
        self.movies = []

    @classmethod 
    def get_directors_movies(cls):
        query = "SELECT * FROM directors JOIN movies ON directors.id = director_id"
        all_directors_movies = connectToMySQL("directors_movies").query_db(query) 
        directors_movies = []

        for dirs_movs in all_directors_movies:
            dir_instance = Director(dirs_movs)

            movie_data = {
                "id": dirs_movs['id'],
                "title": dirs_movs['title'],
                "box_office": dirs_movs['box_office'],
                "director_id": dirs_movs['director_id'],
                "created_at": dirs_movs['movies.created_at'],
                "updated_at": dirs_movs['movies.updated_at'],
            } 

            dir_instance.movie = Movie(movie_data) 
            directors_movies.append(dir_instance) 
        return directors_movies 

    @classmethod 
    def get_director_movies(cls,data):
        query = "SELECT * FROM directors JOIN movies ON directors.id = director_id WHERE director_id = %(id)s"
        all_director_movies = connectToMySQL("directors_movies").query_db(query, data) 

        director = cls(all_director_movies[0]) 

        for dir_movs in all_director_movies:
            movie_data = {
                "id": dir_movs['id'],
                "title": dir_movs['title'],
                "box_office": dir_movs['box_office'],
                "director_id": dir_movs['director_id'],
                "created_at": dir_movs['movies.created_at'],
                "updated_at": dir_movs['movies.updated_at'],
            }  
            director.movies.append(Movie(movie_data)) 
        return director 