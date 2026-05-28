import sqlite3
import pandas as pd

def run_custom_query(db_path="database/movies.db"):
    
    print("CUSTOM QUERY TOOL LOADED")

    print("\nEnter your SQL query below.")
    print("Type 'exit' to quit.\n")

    while True:

        query = input("SQL Query > ")

        if query.lower() == "exit":
            print("Exiting query tool.")
            break
        try:

            conn = sqlite3.connect(db_path)

            print(f"Connected to: {db_path}")

            df = pd.read_sql(query, conn)

            conn.close()

            print("\nQuery Results:\n")

            print(df)

            print(f"\nRows returned: {len(df)}\n")

        except Exception as e:

            print(f"\nError: {e}\n")