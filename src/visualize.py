import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def plot_movies_by_year(db_path="database/movies.db"):

    conn = sqlite3.connect(db_path)

    query = """
    SELECT release_year, COUNT(*) as movie_count
    FROM movies
    GROUP BY release_year
    ORDER BY release_year
    """

    df = pd.read_sql(query, conn)

    conn.close()

    plt.figure()

    plt.bar(df["release_year"], df["movie_count"])

    plt.xlabel("Release Year")
    plt.ylabel("Number of Movies")
    plt.title("Movies by Release Year")

    plt.savefig("outputs/charts/movies_by_year.png")

    plt.close()