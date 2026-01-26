from langchain_community.vectorstores import FAISS
from langchain_aws import BedrockEmbeddings

def build_vector_store(docs):
    embeddings = BedrockEmbeddings(
        model_id="amazon.titan-embed-text-v1",
        region_name="us-east-1"
    )
    return FAISS.from_documents(docs, embeddings)
