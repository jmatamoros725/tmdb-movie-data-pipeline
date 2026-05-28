import requests 
from src.config import TMDB_API_KEY, BASE_URL

def fetch_popular_movies(pages=5):
    all_results = []

    for page in range(1, pages + 1):    
        
        endpoint = f"{BASE_URL}/movie/popular"

        params = {
            "api_key": TMDB_API_KEY,
            "language": "en-US",
            "page": page
        }

        response = requests.get(endpoint, params=params)
        response.raise_for_status()

        data = response.json()
        all_results.extend(data.get("results", []))

    
    return {"results": all_results}