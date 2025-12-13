#!/usr/bin/env python3
"""
Test script to verify all imports work correctly.
"""

import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

print("=" * 60)
print("🧪 Testing RAG Agent Imports")
print("=" * 60)
print()

# Test 1: Import OpenAI
print("1. Testing OpenAI import...")
try:
    from openai import OpenAI

    print("   ✅ OpenAI imported successfully")
except ImportError as e:
    print(f"   ❌ Failed: {e}")
    sys.exit(1)

# Test 2: Import LangChain components
print("\n2. Testing LangChain imports...")
try:
    from langchain_community.document_loaders import PyPDFLoader
    from langchain_community.embeddings import OpenAIEmbeddings
    from langchain_community.vectorstores import Chroma
    from langchain_text_splitters import RecursiveCharacterTextSplitter

    print("   ✅ LangChain components imported successfully")
except ImportError as e:
    print(f"   ❌ Failed: {e}")
    sys.exit(1)

# Test 3: Import agent config
print("\n3. Testing agent.agent_config import...")
try:
    from agent.agent_config import create_rag_agent

    print("   ✅ agent.agent_config imported successfully")
except ImportError as e:
    print(f"   ❌ Failed: {e}")
    print(f"   Current sys.path: {sys.path}")
    sys.exit(1)

# Test 4: Import agent tools
print("\n4. Testing agent.tools imports...")
try:
    from agent.tools.fn_ingest import fn_ingest
    from agent.tools.fn_retrieve import fn_retrieve

    print("   ✅ agent.tools imported successfully")
except ImportError as e:
    print(f"   ❌ Failed: {e}")
    sys.exit(1)

# Test 5: Import Streamlit
print("\n5. Testing Streamlit import...")
try:
    import streamlit

    print("   ✅ Streamlit imported successfully")
except ImportError as e:
    print(f"   ❌ Failed: {e}")
    sys.exit(1)

# Test 6: Import dotenv
print("\n6. Testing python-dotenv import...")
try:
    from dotenv import load_dotenv

    print("   ✅ python-dotenv imported successfully")
except ImportError as e:
    print(f"   ❌ Failed: {e}")
    sys.exit(1)

# Test 7: Check for .env file
print("\n7. Checking for .env file...")
env_file = Path(".env")
if env_file.exists():
    print("   ✅ .env file exists")
    load_dotenv()
    import os

    if os.getenv("OPENAI_API_KEY"):
        print("   ✅ OPENAI_API_KEY is set")
    else:
        print("   ⚠️  OPENAI_API_KEY not found in .env")
else:
    print("   ⚠️  .env file not found (you'll need to create it)")

# Test 8: Check data directory
print("\n8. Checking data directory...")
data_dir = Path("data")
if data_dir.exists():
    pdf_files = list(data_dir.glob("*.pdf"))
    print(f"   ✅ data/ directory exists with {len(pdf_files)} PDF(s)")
    for pdf in pdf_files:
        print(f"      • {pdf.name}")
else:
    print("   ⚠️  data/ directory not found")

# Test 9: Check store directory
print("\n9. Checking store directory...")
store_dir = Path("store")
if store_dir.exists():
    print("   ✅ store/ directory exists")
else:
    print("   ℹ️  store/ directory will be created on first ingestion")

print()
print("=" * 60)
print("✅ All import tests passed!")
print("=" * 60)
print()
print("Next steps:")
print("  1. Make sure .env file has your OPENAI_API_KEY")
print("  2. Generate sample PDFs: python3 create_sample_pdfs_simple.py")
print("  3. Run the app: streamlit run ui/app.py")
print()
