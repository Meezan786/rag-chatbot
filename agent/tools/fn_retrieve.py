# agent/tools/fn_retrieve.py
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma


def fn_retrieve(query: str, k: int = 3):
    """
    Retrieve most relevant text chunks using vector search.
    """

    vectordb = Chroma(
        persist_directory="./store", embedding_function=OpenAIEmbeddings()
    )

    docs = vectordb.similarity_search(query, k=k)

    return {"chunks": [d.page_content for d in docs]}
