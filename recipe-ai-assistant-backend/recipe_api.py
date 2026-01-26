import requests
import boto3
import json

def get_spoonacular_key():
    client = boto3.client("secretsmanager", region_name="us-east-1")
    secret = client.get_secret_value(
        SecretId="prod/my-app/api-keys" 
    )
    return json.loads(secret["SecretString"])["SPOONACULAR_KEY"]


def fetch_recipes(query, diet=""):
    api_key = get_spoonacular_key()

    url = "https://api.spoonacular.com/recipes/complexSearch"
    params = {
        "apiKey": api_key,
        "query": query,
        "diet": diet,
        "number": 5,
        "addRecipeInformation": True
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    return response.json().get("results", [])
