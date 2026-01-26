from langchain_core.documents import Document

def to_docs(recipes):
    docs = []
    for r in recipes:
        ingredients = ", ".join(
            [i["original"] for i in r.get("extendedIngredients", [])]
        )

        text = f"""
        Title: {r.get('title')}
        Ingredients: {ingredients}
        Instructions: {r.get('instructions')}
        """

        docs.append(Document(page_content=text))
    return docs
