def run_rag(query, vector_db, llm_call):
    docs = vector_db.similarity_search(query, k=3)

    context = "\n\n".join([d.page_content for d in docs])

    prompt = f"""
    You are a professional chef assistant.

    Context:
    {context}

    Question:
    {query}

    Answer clearly and concisely.
    """

    return llm_call(prompt)
