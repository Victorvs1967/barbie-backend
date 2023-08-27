import random
from flask import jsonify

from app import app, data
from app.data import barbie_movies


@app.route('/api/movies', methods=['GET'])
def get_movies():
  return jsonify(barbie_movies)

@app.route('/api/random_movie', methods=['GET'])
def get_ramdom_movie():
  random_movie = random.choice(barbie_movies)
  return jsonify(random_movie)