# import 'os': a built-in Python module that lets your program interact with the operating system
import os 
# reads environment variables 
# works with file paths 
# navigates directories
# accesses system-level information

# import function 'load_dotenv' from 'python-dotenv' package
from dotenv import load_dotenv 
# reads a .env file and loads the variables inside it into your system's environment

load_dotenv()
# looks for .env file in project directory
# reads the key-value pairs
# temporarily injects them into the environment for that session

# retrieves the value of the environment variable named "TMDB_API_KEY" and assigns ito the Python variable 'TMDB_API_KEY'
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

# saves the base url as a variable that can be reproduced
BASE_URL = "https://api.themoviedb.org/3"