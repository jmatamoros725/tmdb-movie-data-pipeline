import sqlite3
import pandas as pd

def get_top_rated_movies(db_path="database/movies.db"):
    
    conn = sqlite3.connect(db_path)

    query = """
    SELECT
        title,
        release_year,
        vote_average,
        vote_count
    FROM movies
    ORDER BY vote_average DESC
    LIMIT 10
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df

def get_most_popular_movies(db_path="database/movies.db"):

    conn = sqlite3.connect(db_path)

    query = """
    SELECT
        title,
        popularity,
        release_year
    FROM movies
    ORDER BY popularity DESC
    LIMIT 10
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df

def get_most_voted_movies(db_path="database/movies.db"):

    conn = sqlite3.connect(db_path)

    query = """
    SELECT
        title,
        vote_count,
        vote_average
    FROM movies
    ORDER BY vote_count DESC
    LIMIT 10
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df