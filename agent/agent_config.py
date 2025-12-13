# agent/agent_config.py
import os
import sys

from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

from agent.tools.fn_ingest import fn_ingest
from agent.tools.fn_retrieve import fn_retrieve


def get_rag_tools():
    """Return the tools configuration for RAG operations."""
    return [
        {
            "type": "function",
            "function": {
                "name": "fn_ingest",
                "description": "Ingest PDF documents and store embeddings",
                "parameters": {
                    "type": "object",
                    "properties": {"file_path": {"type": "string"}},
                    "required": ["file_path"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "fn_retrieve",
                "description": "Retrieve relevant text chunks using vector search",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string"},
                        "k": {"type": "number"},
                    },
                    "required": ["query"],
                },
            },
        },
    ]


def get_rag_instructions():
    """Return the system instructions for RAG operations."""
    return """
    You are a Retrieval-Augmented Generation (RAG) AI.
    Use these tools STRICTLY as required:
    - fn_ingest → to load documents
    - fn_retrieve → to fetch relevant chunks

    Always use retrieved chunks to answer questions.
    If answer cannot be found, say "I don't know".
    """


def create_rag_agent():
    """
    Initialize the RAG agent (now just returns configuration for Responses API).
    The Responses API doesn't require pre-creating assistants.
    """
    # Check if API key is set
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Error: OPENAI_API_KEY not found!")
        print("Please create a .env file with: OPENAI_API_KEY=your_key_here")
        sys.exit(1)

    # Return configuration instead of creating an assistant
    return {
        "model": "gpt-4o",
        "tools": get_rag_tools(),
        "instructions": get_rag_instructions(),
    }
