import requests
import boto3
import json
import logging

logger = logging.getLogger(__name__)

_SPOONACULAR_KEY = None  # cache

def get_spoonacular_key():
    global _SPOONACULAR_KEY

    if _SPOONACULAR_KEY:
        return _SPOONACULAR_KEY

    try:
        client = boto3.client(
            "secretsmanager",
            region_name="us-west-2"
        )

        response = client.get_secret_value(
            SecretId="prod/my-app/api-keys"
        )

        secret_dict = json.loads(response["SecretString"])
        _SPOONACULAR_KEY = secret_dict["SPOONACULAR_API_KEY"]

        return _SPOONACULAR_KEY

    except Exception as e:
        logger.error("Failed to load Spoonacular API key", exc_info=True)
        raise RuntimeError("Secrets Manager error") from e


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

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json().get("results", [])

    except requests.exceptions.RequestException as e:
        logger.error("Spoonacular API error", exc_info=True)
        raise RuntimeError("Recipe API failed") from e
