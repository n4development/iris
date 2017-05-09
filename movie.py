import webbrowser


class Movie():
    """
    this is some desc about this awesome class

    """
    def __init__(self, movie_title, moview_s, poster_img, trailer_youtube):
        self.title = movie_title
        self.storyline = moview_s
        self.poster = poster_img
        self.youtube = trailer_youtube
    def show_trailer(self):
        webbrowser.open(self.youtube)