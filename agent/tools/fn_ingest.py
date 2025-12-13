# agent/tools/fn_ingest.py
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter


def fn_ingest(file_path: str):
    """
    Ingest documents: load → chunk → embed → store in Chroma DB.
    """

    loader = PyPDFLoader(file_path)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)

    vectordb = Chroma.from_documents(
        documents=chunks, embedding=OpenAIEmbeddings(), persist_directory="./store"
    )

    vectordb.persist()

    return {
        "status": "success",
        "message": f"Ingested: {file_path}",
        "chunks": len(chunks),
    }
