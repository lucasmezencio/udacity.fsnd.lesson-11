"""
Media module
"""


class Movie(object):
    """Holds infos about a Movie

    Args:
        title: Movie's title
        storyline: Movie's storyline
        poster_image_url: Movie's poster image URL
        trailer_youtube_url: Movie's trailer Youtube URL
    Behavior:
        Create an instance of the Movie class
    Returns:
        void
    """

    def __init__(self, title, storyline, poster_image_url,
                 trailer_youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
