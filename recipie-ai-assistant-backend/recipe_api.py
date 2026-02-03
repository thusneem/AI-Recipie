import requests
import boto3
import json
import logging

logger = logging.getLogger(__name__)

_SPOONACULAR_KEY = None  # cache

def get_spoonacular_key():
    client = boto3.client("secretsmanager", region_name="us-east-1")
    response = client.get_secret_value(SecretId="prod/my-app/api-keys")
    secret_dict = json.loads(response["SecretString"])

    api_key = (
        secret_dict.get("SPOONACULAR_API_KEY")
        or secret_dict.get("SPOONACULAR_KEY")
        or secret_dict.get("spoonacular_api_key")
    )

    if not api_key:
        raise RuntimeError("Spoonacular API key not found in Secrets Manager")

    return api_key


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
