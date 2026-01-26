import requests
from config import SPOONACULAR_KEY

def fetch_recipes(query, diet=""):
    url = "https://api.spoonacular.com/recipes/complexSearch"
    params = {
        "apiKey": SPOONACULAR_KEY,
        "query": query,
        "diet": diet,
        "number": 5,
        "addRecipeInformation": True
    }
    return requests.get(url, params=params).json()["results"]
