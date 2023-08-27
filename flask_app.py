import random
from flask import Flask
from flask import jsonify
from flask_cors import CORS


barbie_movies = [
  {
    "id": 1,
    "title": "Barbie in the Nutcracker",
    "year": 2001,
    "director": "Owen Hurley",
    "cast": ["Kelly Sheridan", "Kirbi Morrow", "Tim Curry"],
    "synopsis": "A Barbie version of E.T.A. Hoffmann's tale of the..."
  },
  {
    "id": 2,
    "title": "Barbie as Rapunzel",
    "year": 2002,
    "director": "Owen Hurley",
    "cast": ["Kelly Sheridan", "Anjelica Hutson", "Cree Summer"],
    "synopsis": "Barbie is an artist who paints her way out of..."
  },
  {
    "id": 3,
    "title": "Barbie of Swan Lake",
    "year": 2003,
    "director": "Owen Hurley",
    "cast": ["Kelly Sheridan", "Mark Hildreth", "Kelsey Grammer"],
    "synopsis": "Barbie comes to life in her third animated movie..."
  },
]

app = Flask(__name__)
CORS(app)

@app.route('/api/movies', methods=['GET'])
def get_movies():
  return jsonify(barbie_movies)


@app.route('/api/random_movie', methods=['GET'])
def get_ramdom_movie():
  random_movie = random.choice(barbie_movies)
  return jsonify(random_movie)


if __name__ == '__main__':
  app.run()