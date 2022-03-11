import re
from flask import Flask, redirect, render_template, request
from src.repositories.movie_repository import movie_repository_singleton

app = Flask(__name__)


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1
    return render_template('list_all_movies.html', list_movies_active=True)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    # TODO: Feature 2
    movieInfo = None
    t = request.form.get('t')
    d = request.form.get('d')
    r = request.form.get('r')
    
    if t != None and t != '' and d != None and d != '' and r != None and r != '':
        movieInfo = movie_repository_singleton.create_movie(t, d, int(r))
    else:
        return render_template('create_movies_form.html', create_rating_active=True)
    
    # After creating the movie in the database, we redirect to the list all movies page
    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    return render_template('search_movies.html', search_active=True)