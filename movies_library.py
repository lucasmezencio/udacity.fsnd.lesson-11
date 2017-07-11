"""
Entertainment Center
"""

from media import Movie
from generator import Generator

the_prestige = Movie('The Prestige',
                     'It\'s Magic!',
                     'https://upload.wikimedia.org/wikipedia/en'
                     '/d/d2/Prestige_poster.jpg',
                     'http://youtube.com/watch?v=o4gHCmTQDVI')

arrival = Movie('Arrival',
                'Aliens! What?',
                'https://upload.wikimedia.org/wikipedia/en/'
                'd/df/Arrival%2C_Movie_Poster.jpg',
                'https://www.youtube.com/watch?v=ZLO4X6UI8OY')

donnie = Movie('Donnie Darko',
               'Time travel and consequences.',
               'https://upload.wikimedia.org/wikipedia/en/'
               'd/db/Donnie_Darko_poster.jpg',
               'https://www.youtube.com/watch?v=ZZyBaFYFySk')

imitation_game = Movie('The Imitation Game',
                       'Programming! Alan Turing!',
                       'https://upload.wikimedia.org/wikipedia/en/'
                       '5/5e/The_Imitation_Game_poster.jpg',
                       'https://www.youtube.com/watch?v=S5CjKEFb-sM')

movies = [the_prestige, arrival, donnie, imitation_game]

page_generator = Generator()
page_generator.open_movies_page(movies)
