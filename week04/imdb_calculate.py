import math
import random

movie_catalog = [{"name": "Batman: Under the Red Hood", "genre": "Animation/Action", "rating": 7.6},
                 {"name": "Wall-E", "genre": "Animation/Adventure", "rating": 8.4},
                 {"name": "Spiderman: Into the Spider-Verse", "genre": "Animation/Action", "rating": 8.4},
                 {"name": "Inception ", "genre": "Action/Sci-Fi", "rating": 8.8},
                 {"name": "Interstellar", "genre": "Sci-Fi/Drama", "rating": 8.7},
                 {"name": "Star Wars: Fantom Menace", "genre": "Sci-Fi/Action", "rating": 6.5},]

print("Welcome to the IMDB Movie Rating and Analysis Tool!")

username = input ("Please enter your name:").strip()
print(f"Hello, {username}! Selecting a movie from our catalog.")

selected_movie = random.choice(movie_catalog)
imdb_rating = selected_movie["rating"]

raw_compatibility = random.uniform(80.5, 99.9)
match_percentage = math.floor(raw_compatibility)

print("\n " + "=" *45)
print("Movie Analysis Report")
print("=" * 45)
print(f"Movie Name: {selected_movie['name']}")
print(f"Genre: {selected_movie['genre']}")
print(f"IMDB Rating: {imdb_rating}")
print(f"Profile Match : {match_percentage}%")
print("=" * 45)

if imdb_rating >= 8.5:
    print("Recommendation: This movie is a masterpiece, you should definitely watch it!")
else:
    print("Recommendation: A great choice for a pleasant movie night.")