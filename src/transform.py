import pandas as pd

def transform_movie_data(raw_json):
    movies = raw_json.get("results", [])
    df = pd.DataFrame(movies)

    selected_columns = [
        "id",
        "title",
        "release_date",
        "vote_average",
        "vote_count",
        "popularity"
    ]

    df = df[selected_columns]

    df["release_date"] = pd.to_datetime(df["release_date"], errors='coerce')
    df["release_year"] = df["release_date"].dt.year
    df["weighted_score"] = df["vote_average"] * df["vote_count"]

    df = df.dropna(subset=["title"])

    return df