import sqlite3

def load_to_sqlite(df, db_path="database/movies.db"):
    conn = sqlite3.connect(db_path)
    df.to_sql("movies", conn, if_exists="replace", index=False)
    conn.close()

    return len(df)