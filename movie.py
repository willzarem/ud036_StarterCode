import webbrowser


# A class that creates a moview from it's title, storyline, poster and trailer
class Movie:
    # The constructor of the object with it's params
    def __init__(self, title, storyline, poster_image_url,
                 trailer_youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    # A function that will open up a browser window and play the movie trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
