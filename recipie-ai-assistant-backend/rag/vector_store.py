from langchain_community.vectorstores import FAISS
from langchain_aws import BedrockEmbeddings

def build_vector_store(docs):
    docs = [d for d in docs if d.page_content and d.page_content.strip()]
    if not docs:
        raise ValueError("No valid documents to embed")

    embeddings = BedrockEmbeddings(
        model_id="amazon.titan-embed-text-v1",
        region_name="us-west-2"
    )
    print(len(embeddings.embed_query("ping")))
    return FAISS.from_documents(docs, embeddings)


