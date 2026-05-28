from src.extract import fetch_popular_movies
from src.transform import transform_movie_data
from src.load import load_to_sqlite
from src.visualize import plot_movies_by_year

def run_pipeline():
    raw_data = fetch_popular_movies()
    df = transform_movie_data(raw_data)
    rows = load_to_sqlite(df)
    plot_movies_by_year()

    print(f"Pipeline complete. Rows loaded: {rows}")

if __name__ == "__main__":
    run_pipeline()