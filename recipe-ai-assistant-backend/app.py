from flask import Flask, request, jsonify
from flask_cors import CORS

from recipe_api import fetch_recipes
from rag.documents import to_docs
from rag.vector_store import build_vector_store
from rag.rag_pipeline import run_rag
from bedrock import call_bedrock  # your Bedrock wrapper

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})

@app.route("/")
def health():
    return "app is deployed", 200


@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    query = data["question"]
    diet = data.get("diet", "")

    recipes = fetch_recipes(query, diet)
    docs = to_docs(recipes)
    vector_db = build_vector_store(docs)

    answer = run_rag(query, vector_db, call_bedrock)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
