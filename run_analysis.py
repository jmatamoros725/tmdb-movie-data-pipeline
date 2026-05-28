from src.analysis import *

top_movies = get_top_rated_movies()

print("\nTop Rated Movies:")
print(top_movies)

most_popular_movies = get_most_popular_movies()

print("\nMost Popular Movies:")
print(most_popular_movies)

most_votes = get_most_voted_movies()

print("\nMovies with the Most Votes:")
print(most_votes)