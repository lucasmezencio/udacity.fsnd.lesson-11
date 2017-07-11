"""
HTML Generator
"""

import webbrowser
import os
import re


class Generator(object):
    """Generate HTML for the web page"""

    def load_template(self, template_name):
        """Load template from HTML file"""
        path = os.getcwd()
        template_file = open('%s/templates/%s.html' % (path, template_name))
        content = template_file.read()

        template_file.close()

        return content

    def create_movie_tiles_content(self, movies):
        """Parse and return movie tiles content"""

        # The HTML content for this section of the page
        content = ''

        for movie in movies:
            # Extract the youtube ID from the url
            youtube_id_match = re.search(
                r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
            youtube_id_match = youtube_id_match or re.search(
                r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
            trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                                  else None)

            movie_tile_content = self.load_template('tile')

            # Append the tile for the movie with its content filled in
            content += movie_tile_content.format(
                movie_title=movie.title,
                poster_image_url=movie.poster_image_url,
                trailer_youtube_id=trailer_youtube_id,
                storyline=movie.storyline
            )

        return content

    def open_movies_page(self, movies):
        """Gather all page pieces together and open a web browser"""

        # Create or overwrite the output file
        output_file = open('movies_library.html', 'w')

        main_page_head = self.load_template('header')
        main_page_content = self.load_template('content')

        # Replace the movie tiles placeholder generated content
        rendered_content = main_page_content.format(
            movie_tiles=self.create_movie_tiles_content(movies))

        # Output the file
        output_file.write(main_page_head + rendered_content)
        output_file.close()

        # open the output file in the browser (in a new tab, if possible)
        url = os.path.abspath(output_file.name)
        webbrowser.open('file://' + url, new=2)
