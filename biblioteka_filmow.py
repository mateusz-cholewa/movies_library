from faker import Faker
fake = Faker()

class Movie_Library:
    def __init__(self, title, year, type, number_of_plays):
        self.title = title
        self.year = year
        self.type = type
        self.views = 0

    def play(self, view = 1):
        self.views += view


class Series_Library(Movie_Library):
    def __init__(self, episode_number, season_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_numer = episode_number
        self.season_number = season_number

    def play(self, view = 1):
        self.views += view

print(fake.word().capitalize())