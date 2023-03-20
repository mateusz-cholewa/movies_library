from faker import Faker
fake = Faker()
import random

class Movie_Library:
    def __init__(self, title, year, type, views = 0):
        self.title = title
        self.year = year
        self.type = type
        self.views = views
        

    def play(self):
        self.views += 1

    def __str__(self):
        return f"{self.title} ({self.year})"
    

class Series_Library(Movie_Library):
    def __init__(self, episode_number, season_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_numer = episode_number
        self.season_number = season_number

    def play(self):
        self.views += 1

    def __str__(self):
        return f"{self.title} S{self.season_number:02d}E{self.episode_numer:02d}"

    
class Library:
    def __init__(self):
        self.titles = []

    def add_title(self, title):
        self.titles.append(title)

    def get_movies(self):
        return sorted(filter(lambda x: isinstance(x, Movie_Library), self.titles), key=lambda x: x.title)
    
    def get_series(self):
        return sorted(filter(lambda x: isinstance(x, Series_Library), self.titles), key = lambda x: x.title)
    
    def serach(self, title):
        return list(filter(lambda x: x.title.lower() == title.lower(), self.titles))
    
    def generate_views(self):
        title = random.choice(self.titles)
        title.play()
        title.views += random.randint(0,100)

    def generate_views_n_times(self, n):
        for i in range(n):
            self.generate_views()

    def top_titles(self, n):
        return sorted(self.titles, key = lambda x: x.views, reverse = True) [:n]
    
library = Library()

for _ in range(10):
    library.add_title(Movie_Library(title=fake.word().capitalize(), year=fake.year(), type=fake.word().capitalize()))
    library.add_title(Series_Library(title=fake.word().capitalize(), year=fake.year(), type=fake.word().capitalize(), episode_number=fake.random_int(1,20), season_number=fake.random.randint(1,5)))
    
library.generate_views_n_times(5)

print("Movies")
for movie in library.get_movies():
    print(f" - {movie}")

print("TV Series")
for series in library.get_series():
    print(f" - {series}")

top_titles = library.top_titles(2)
print(f"Top titles:")
for title in top_titles:
    print(f"- {title.title} ({title.views} views)")



            




    


