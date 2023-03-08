from faker import Faker
fake = Faker()

class Movie_Library:
    def __init__(self, title, year, type):
        self.title = title
        self.year = year
        self.type = type
        self.views = 0

    def play(self, view = 1):
        self.views += view

    def __str__(self):
        return f"Oglądasz {self.title} z roku {self.year}"


class Series_Library(Movie_Library):
    def __init__(self, episode_number, season_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_numer = episode_number
        self.season_number = season_number

    def play(self, view = 1):
        self.views += view

    def __str__(self):
        return f"Oglądasz {self.title} S{self.season_number:02d}E{self.episode_numer:02d}"

library = []

for _ in range(5):
    films = Movie_Library(title=fake.word().capitalize(), year=fake.year(), type=fake.word().capitalize())
    library.append(films)
    series = Series_Library(title=fake.word().capitalize(), year=fake.year(), type=fake.word().capitalize(), episode_number=fake.random_int(1,20), season_number=fake.random_digit())
    library.append(series)

    def get_movies():
        movies = []
        for obj in library:
            if season_number not in library:
                movies.append(obj)
        return sorted(movies)

    def get_series():
        series = []
        for obj in library:
            if season_number > 0:
                series.append(obj)
        return sorted(series)

print(series.get_series())
    


