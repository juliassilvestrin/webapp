import json
import os.path
import sqlite3

def dict_factory(cursor, row):
 fields = []
 # Extract column names from cursor description
 for column in cursor.description:
    fields.append(column[0])

 # Create a dictionary where keys are column names and values are row values
 result_dict = {}
 for i in range(len(fields)):
    result_dict[fields[i]] = row[i]

 return result_dict


class MoviesDB:
    def __init__(self,filename):
        #connect to DB file
        self.connection = sqlite3.connect(filename)
        self.connection.row_factory = dict_factory
        #use the connection instance to perform db operations
        #create a cursor instance for the connection
        self.cursor = self.connection.cursor()

    def getMovies(self): #all
        #now that we have an acess point we can fetch all or one
        #ONLY applicable use of fetch is following a SELECT query
        self.cursor.execute("SELECT * FROM movies")
        movies = self.cursor.fetchall()
        return movies
    
    def getMovie(self,movie_id):
        data = [movie_id] #array
        self.cursor.execute("SELECT * FROM movies WHERE id = ?", data)
        movie = self.cursor.fetchone()
        return movie
    
    def createMovie(self,name,review,rating, genre, release_year):
        data = [name,review,rating, genre, release_year]
        #add a new rollercoaster to our db
        self.cursor.execute("INSERT INTO movies(name, review, rating, genre, release_year)VALUES(?, ?, ?, ?, ?)", data)
        self.connection.commit()

    def updateMovie(self,movie_id,name,review,rating, genre, release_year):
       data = [movie_id, name, review, rating, genre, release_year]
       self.cursor.execute("UPDATE movies SET name = ?, review = ?, rating = ?, genre = ?, release_year = ? WHERE id = ?", data)
       self.connection.commit()

    def deleteMovie(self, movie_id):
       data = [movie_id]
       self.cursor.execute("DELETE FROM movies WHERE id = ?", data)
       self.connection.commit()
