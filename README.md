# 🤖 RAG Chatbot - Intelligent Document Q&A System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-green.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Web--UI-red.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

*A production-ready Retrieval-Augmented Generation (RAG) chatbot that answers questions about your documents using advanced AI.*

[🚀 Live Demo](#-quick-start) • [📖 Documentation](#-architecture) • [🛠️ Installation](#-installation)

</div>

---

## 📋 Table of Contents

- [✨ Overview](#-overview)
- [🎯 Features](#-features)
- [🏗️ Architecture](#️-architecture)
- [🛠️ Installation](#️-installation)
- [🚀 Quick Start](#-quick-start)
- [📁 Project Structure](#-project-structure)
- [🛠️ Technologies](#️-technologies)
- [📖 Usage](#-usage)
- [🔧 Configuration](#-configuration)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

---

## ✨ Overview

**RAG Chatbot** is a sophisticated AI-powered document question-answering system that combines the power of large language models with intelligent document retrieval. Upload your PDF documents and get accurate, context-aware answers to your questions.

### 🎯 What It Does

- **📄 Document Ingestion**: Seamlessly process and index PDF documents
- **🧠 Smart Retrieval**: Find relevant information using vector similarity search
- **💬 Intelligent Q&A**: Generate accurate answers based on document content
- **🌐 Web Interface**: User-friendly Streamlit-based chat interface
- **⚡ Fast Processing**: Optimized for quick responses and efficient storage

### 🚀 Use Cases

- **Research Assistant**: Ask questions about academic papers, reports, or documentation
- **Customer Support**: Build knowledge bases from product manuals and FAQs
- **Legal Research**: Query legal documents and case files
- **Educational Tool**: Create interactive study guides from textbooks
- **Business Intelligence**: Analyze reports, memos, and business documents

---

## 🎯 Features

### Core Capabilities
- ✅ **PDF Processing**: Extract and chunk text from PDF documents
- ✅ **Vector Embeddings**: Convert text to semantic vectors using OpenAI
- ✅ **Similarity Search**: Efficient retrieval using ChromaDB vector database
- ✅ **Contextual Answers**: Generate responses based on retrieved document chunks
- ✅ **Multi-turn Conversations**: Maintain conversation context
- ✅ **Real-time Streaming**: Live response generation in the UI

### User Experience
- 🎨 **Modern UI**: Clean, responsive Streamlit interface
- 📱 **Cross-platform**: Works on desktop and mobile browsers
- ⚡ **Fast Responses**: Optimized for low-latency interactions
- 🔄 **Real-time Updates**: Live status updates during processing
- 💾 **Persistent Storage**: Documents remain indexed between sessions

### Developer Features
- 🏗️ **Modular Architecture**: Clean separation of concerns
- 🛠️ **Custom Tools**: Extensible function calling system
- 📊 **Monitoring**: Built-in logging and error handling
- 🔧 **Configuration**: Environment-based settings management
- 🧪 **Testing**: Comprehensive test coverage and validation

---

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   User Query    │───▶│  Chat Interface │───▶│  LLM Processing │
│                 │    │   (Streamlit)   │    │  (OpenAI GPT)   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                │                        │
                                ▼                        ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ Document Store  │◀───│  Vector Search  │◀───│  Embedding Gen  │
│    (ChromaDB)   │    │   (Similarity)  │    │   (OpenAI)      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                ▲                        ▲
                                │                        │
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   PDF Parser    │───▶│  Text Chunker   │───▶│  Document Q&A   │
│    (PyPDF)      │    │   (LangChain)   │    │    (RAG)        │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### Data Flow

1. **Document Ingestion**: PDFs → Text extraction → Chunking → Embeddings → Vector DB
2. **Query Processing**: User question → Vector search → Context retrieval → LLM generation
3. **Response Generation**: Retrieved chunks + question → AI reasoning → Contextual answer

### Key Components

- **Agent Core**: Orchestrates the RAG pipeline and tool execution
- **Document Tools**: `fn_ingest` for indexing, `fn_retrieve` for search
- **Vector Store**: ChromaDB for efficient similarity search
- **Web Interface**: Streamlit for user interaction
- **LLM Integration**: OpenAI GPT-4o for intelligent responses

---

## 🛠️ Installation

### Prerequisites

- **Python**: 3.8 or higher
- **OpenAI Account**: API key with credits ([Get API Key](https://platform.openai.com/api-keys))
- **Git**: Version control system

### Step-by-Step Setup

#### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd rag-chatbot
```

#### 2. Create Virtual Environment
```bash
# Create environment
python -m venv venv

# Activate environment
# macOS/Linux:
source venv/bin/activate

# Windows:
venv\Scripts\activate
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Configure Environment
```bash
# Create .env file
touch .env
```

Add your OpenAI API key to `.env`:
```env
OPENAI_API_KEY=sk-your-api-key-here
```

#### 5. Generate Sample Data (Optional)
```bash
python create_sample_pdfs_simple.py
```

---

## 🚀 Quick Start

### Start the Application

```bash
# Activate virtual environment (if not already activated)
source venv/bin/activate

# Launch the web interface
streamlit run ui/app.py
```

The application will open in your default browser at `http://localhost:8501`.

### Basic Usage

1. **Ingest a Document**:
   ```
   User: Ingest the document data/AI_and_Machine_Learning.pdf
   Bot: ✅ Document ingested successfully!
   ```

2. **Ask Questions**:
   ```
   User: What is machine learning?
   Bot: [Provides detailed answer based on document content]
   ```

3. **Continue the Conversation**:
   ```
   User: How does it relate to deep learning?
   Bot: [Answers based on retrieved context]
   ```

### Sample Documents

The project includes sample PDFs covering:
- Artificial Intelligence & Machine Learning
- Python Programming Guide
- Data Science Fundamentals

---

## 📁 Project Structure

```
rag-chatbot/
├── agent/                          # AI Agent Core
│   ├── __init__.py
│   ├── agent_config.py            # Agent configuration & tools
│   └── tools/                     # Custom functions
│       ├── __init__.py
│       ├── fn_ingest.py           # Document ingestion
│       ├── fn_retrieve.py         # Vector search
│       └── runner.py              # CLI interface
├── ui/                            # User Interface
│   └── app.py                     # Streamlit web app
├── data/                          # Document storage
├── store/                         # Vector database (ChromaDB)
├── .env                           # Environment variables
├── requirements.txt               # Python dependencies
├── create_sample_pdfs_simple.py   # Sample data generator
├── run_app.py                     # Application launcher
├── test_imports.py                # Import validation
└── README.md                      # Documentation
```

---

## 🛠️ Technologies

| Component | Technology | Purpose |
|-----------|------------|---------|
| **AI Model** | OpenAI GPT-4o | Natural language processing & generation |
| **Embeddings** | OpenAI text-embedding-ada-002 | Text vectorization |
| **Vector DB** | ChromaDB | Similarity search & storage |
| **Document Processing** | PyPDF, LangChain | PDF parsing & text chunking |
| **Web Framework** | Streamlit | Interactive user interface |
| **Language** | Python 3.8+ | Core programming language |
| **Environment** | python-dotenv | Configuration management |

### Dependencies

- **Core AI**: `openai`, `langchain-openai`
- **Document Processing**: `pypdf`, `langchain-community`
- **Vector Operations**: `chromadb`, `langchain-text-splitters`
- **Web Interface**: `streamlit`
- **Utilities**: `python-dotenv`, `fpdf2`

---

## 📖 Usage

### Document Management

#### Adding Documents
```python
# Ingest a PDF document
"Ingest the document data/your_document.pdf"
```

#### Supported Formats
- PDF documents (primary)
- Text extraction from various layouts
- Automatic chunking and indexing

### Query Interface

#### Natural Language Queries
- "What are the main concepts in this document?"
- "Summarize the key findings"
- "Explain the methodology used"

#### Contextual Follow-ups
- "How does this relate to...?"
- "Can you elaborate on...?"
- "What are the implications of...?"

### Advanced Features

#### Custom Tools
The system includes two main tools:

1. **Document Ingestion** (`fn_ingest`):
   - Loads PDF content
   - Splits into semantic chunks
   - Generates embeddings
   - Stores in vector database

2. **Context Retrieval** (`fn_retrieve`):
   - Performs similarity search
   - Returns relevant document chunks
   - Supports configurable result count

---

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
# Required: OpenAI API Configuration
OPENAI_API_KEY=sk-your-api-key-here

# Optional: Model Configuration
OPENAI_MODEL=gpt-4o
EMBEDDING_MODEL=text-embedding-ada-002

# Optional: Vector Database Configuration
VECTOR_DB_PATH=./store
CHUNK_SIZE=500
CHUNK_OVERLAP=50
```

### Customization Options

#### Chunking Strategy
Modify `agent/tools/fn_ingest.py`:
```python
# Adjust chunk size and overlap
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,      # Characters per chunk
    chunk_overlap=50     # Overlap between chunks
)
```

#### Embedding Model
Update `agent/agent_config.py`:
```python
# Change embedding model
vectordb = Chroma.from_documents(
    documents=chunks,
    embedding=OpenAIEmbeddings(model="text-embedding-3-small")
)
```

#### UI Customization
Modify `ui/app.py` for interface changes.

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Development Setup
```bash
# Fork the repository
# Clone your fork
git clone https://github.com/your-username/rag-chatbot.git
cd rag-chatbot

# Create feature branch
git checkout -b feature/amazing-feature
```

### Guidelines

#### Code Style
- Follow PEP 8 Python style guidelines
- Use meaningful variable and function names
- Add docstrings to all functions
- Write comprehensive unit tests

#### Pull Request Process
1. **Test thoroughly** - Ensure all tests pass
2. **Update documentation** - Keep README current
3. **Write clear commit messages** - Explain what and why
4. **Reference issues** - Link related issues in PR description

#### Areas for Contribution
- 🐛 **Bug fixes** - Report and fix issues
- ✨ **New features** - Add document formats, improve UI
- 📚 **Documentation** - Improve guides and examples
- 🧪 **Testing** - Add comprehensive test coverage
- 🎨 **UI/UX** - Enhance user interface and experience

### Testing
```bash
# Run basic import tests
python test_imports.py

# Test individual components
python -m pytest tests/  # If test suite exists
```

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 RAG Chatbot

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 🙏 Acknowledgments

- **OpenAI** for providing powerful language models
- **LangChain** for the excellent RAG framework
- **ChromaDB** for efficient vector storage
- **Streamlit** for the amazing web framework
- **The open-source community** for inspiration and tools

---

## 📞 Support & Community

For questions, issues, or contributions:

- 📖 **Documentation**: This README and inline code comments
- 🐛 **Bug Reports**: Open an issue in the GitHub repository
- 💡 **Feature Requests**: Suggest improvements via GitHub issues
- 🤝 **Contributing**: See the Contributing section above

---

<div align="center">

**Built with ❤️ for the AI community**

⭐ Star this repo if you found it helpful!

[⬆️ Back to Top](#-rag-chatbot---intelligent-document-qa-system)

</div>