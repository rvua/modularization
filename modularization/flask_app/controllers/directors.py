from flask_app import app
from flask import render_template
from flask_app.models.director import Director


@app.route('/')
def index(): 
    directors_movies = Director.get_directors_movies()
    return render_template('index.html', directors_movies=directors_movies)

@app.route('/director/<int:id>')
def director(id): 
    data = {
        "id":id
    }
    director_movies = Director.get_director_movies(data)
    return render_template('director.html', dms=director_movies) 