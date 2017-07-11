"""
Entertainment Center
"""

import os
import json

# Import project related classes
from media import Movie
from generator import Generator

# Get movies list from a JSON file
path = os.getcwd()
movies_file = open('%s/resources/movies.json' % path)
movies_json = json.loads(movies_file.read())
movies_file.close()
movies = []

for movie in movies_json:
    movie_instance = Movie(movie['name'], movie['storyline'],
                           movie['poster_url'], movie['video_url'])
    movies.append(movie_instance)

page_generator = Generator()
page_generator.open_movies_page(movies)
