
from typing import Any
from flask import Flask, request
from moviesdb import MoviesDB


class MyFlask(Flask):
    def add_url_rule(self, rule, endpoint=None, view_func=None, **options):
        return super().add_url_rule(rule, endpoint, view_func, provide_automatic_options=False, **options)


app = MyFlask(__name__)

@app.route("/<path:path>", methods=["OPTIONS"])
def cors_preflight(path):
    return "", 200, {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "PUT, DELETE, GET, POST, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type"
    }



"""@app.route("movies/<int:movie_id>", methods=[""]) #add the methods
def hancle_cors_options(coaster_id): #204 (no content)
    return "", 204, {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Origin": "PUT, DELETE",
        "Access-Control-Allow-Origin": "Content-Type"

    }"""

@app.route("/movies", methods=["GET"] )
def retrieve_movies():
    db = MoviesDB("movies_db.db")
    movies = db.getMovies()
    return movies, 200,  {"Access-Control-Allow-Origin" : "*"}

@app.route("/movies/<int:movie_id>", methods=["GET"] ) #single movie 
def retrieve_movie(movie_id):
    db = MoviesDB("movies_db.db")
    movie = db.getMovie(movie_id)
    if movie:
        return movie, 200,  {"Access-Control-Allow-Origin" : "*"}
    else:
        return f"Movie with {movie_id} not found", 404, {"Access-Control-Allow-Origin" : "*"} 
        


@app.route("/movies", methods=["POST"])
def create_movie():
    print("The request data is: ", request.form)
    name = request.form["name"]
    review = request.form["review"]
    rating = request.form["rating"]
    genre = request.form ["genre"]
    release_year = request.form ["release_year"]
    db = MoviesDB("movies_db.db")
    db.createMovie(name,review,rating, genre, release_year)
    return "Created", 201, {"Access-Control-Allow-Origin" : "*"}

@app.route("/movies/<int:movie_id>", methods=["PUT"])
def update_movie(movie_id):
    print("Updating movie with ID", movie_id)
    db = MoviesDB("movies_db.db")
    movie = db.getMovie(movie_id)
    if movie:
        name = request.form["name"]
        review = request.form["review"]
        rating = request.form["rating"]
        genre = request.form["genre"]
        release_year = request.form["release_year"]
        db.updateMovie(movie_id, name, review, rating, genre, release_year)
        return "Updated", 200, {"Access-Control-Allow-Origin": "*"}
    else:
        return f"Movie with {movie_id} not found", 404, {"Access-Control-Allow-Origin": "*"}

@app.route("/movies/<int:movie_id>", methods=["DELETE"])
def delete_movie(movie_id):
    print("Deleting movie with ID", movie_id)
    db = MoviesDB("movies_db.db")
    movie = db.getMovie(movie_id)
    if movie:
        db.deleteMovie(movie_id)
        return "Deleted", 200, {"Access-Control-Allow-Origin": "*"}
    else:
        return f"Movie with {movie_id} not found", 404, {"Access-Control-Allow-Origin": "*"}


  

def run():
    app.run(port=8080)

if __name__ == "__main__":
    run()

