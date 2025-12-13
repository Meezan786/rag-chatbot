#!/usr/bin/env python3
"""
Simple script to generate sample PDF documents for testing the RAG agent.
Uses fpdf2 library (simpler alternative to reportlab).
"""

import os
import sys


def check_dependencies():
    """Check if required libraries are installed."""
    try:
        from fpdf import FPDF

        return True
    except ImportError:
        print("❌ fpdf2 library not found")
        print("\nInstalling fpdf2...")
        os.system("pip install fpdf2 -q")
        try:
            from fpdf import FPDF

            print("✅ fpdf2 installed successfully")
            return True
        except ImportError:
            print("❌ Failed to install fpdf2")
            print("\nPlease install manually:")
            print("  pip install fpdf2")
            return False


def create_ai_ml_pdf():
    """Create a PDF about Artificial Intelligence and Machine Learning"""
    from fpdf import FPDF

    filename = "data/AI_and_Machine_Learning.pdf"
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 24)
    pdf.cell(0, 20, "Artificial Intelligence and Machine Learning", ln=True, align="C")
    pdf.ln(10)

    # Introduction to AI
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Introduction to AI", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(
        0,
        6,
        "Artificial Intelligence (AI) refers to the simulation of human intelligence in machines "
        "that are programmed to think and learn like humans. AI systems can perform tasks that "
        "typically require human intelligence, such as visual perception, speech recognition, "
        "decision-making, and language translation.",
    )
    pdf.ln(5)

    # What is Machine Learning
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "What is Machine Learning?", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(
        0,
        6,
        "Machine Learning (ML) is a subset of AI that focuses on the development of algorithms "
        "and statistical models that enable computers to improve their performance on a specific "
        "task through experience. Instead of being explicitly programmed, ML systems learn from "
        "data and identify patterns to make decisions with minimal human intervention.",
    )
    pdf.ln(5)

    # Types of Machine Learning
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Types of Machine Learning", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 6, "There are three main types of machine learning:")
    pdf.ln(2)
    pdf.multi_cell(
        0,
        6,
        "1. Supervised Learning: The algorithm learns from labeled training data, making "
        "predictions based on input-output pairs. Examples include classification and regression tasks.",
    )
    pdf.ln(2)
    pdf.multi_cell(
        0,
        6,
        "2. Unsupervised Learning: The algorithm discovers hidden patterns in unlabeled data. "
        "Common techniques include clustering and dimensionality reduction.",
    )
    pdf.ln(2)
    pdf.multi_cell(
        0,
        6,
        "3. Reinforcement Learning: The algorithm learns through trial and error, receiving "
        "rewards or penalties for actions taken in an environment.",
    )
    pdf.ln(5)

    # Deep Learning
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Deep Learning", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(
        0,
        6,
        "Deep Learning is a specialized subset of machine learning that uses artificial neural "
        "networks with multiple layers (deep neural networks). These networks can automatically "
        "learn hierarchical representations of data, making them particularly effective for "
        "complex tasks like image recognition, natural language processing, and speech recognition.",
    )
    pdf.ln(5)

    # Applications
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Applications of AI and ML", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 6, "AI and ML technologies are transforming various industries:")
    pdf.ln(2)
    pdf.multi_cell(
        0, 6, "- Healthcare: Disease diagnosis, drug discovery, personalized treatment"
    )
    pdf.multi_cell(
        0, 6, "- Finance: Fraud detection, algorithmic trading, credit scoring"
    )
    pdf.multi_cell(0, 6, "- Transportation: Autonomous vehicles, route optimization")
    pdf.multi_cell(
        0, 6, "- E-commerce: Recommendation systems, customer service chatbots"
    )
    pdf.multi_cell(0, 6, "- Manufacturing: Predictive maintenance, quality control")

    pdf.output(filename)
    print(f"✓ Created: {filename}")


def create_python_programming_pdf():
    """Create a PDF about Python Programming"""
    from fpdf import FPDF

    filename = "data/Python_Programming_Guide.pdf"
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 24)
    pdf.cell(0, 20, "Python Programming Guide", ln=True, align="C")
    pdf.ln(10)

    # Introduction
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Introduction to Python", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(
        0,
        6,
        "Python is a high-level, interpreted programming language known for its simplicity and "
        "readability. Created by Guido van Rossum and first released in 1991, Python has become "
        "one of the most popular programming languages in the world. Its design philosophy emphasizes "
        "code readability with the use of significant indentation.",
    )
    pdf.ln(5)

    # Key Features
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Key Features of Python", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(
        0, 6, "Python offers several advantages that make it popular among developers:"
    )
    pdf.ln(2)
    pdf.multi_cell(
        0, 6, "- Easy to Learn: Python has a simple syntax that mimics natural language"
    )
    pdf.multi_cell(
        0,
        6,
        "- Versatile: Suitable for web development, data science, automation, AI/ML",
    )
    pdf.multi_cell(
        0, 6, "- Large Standard Library: Comprehensive built-in modules and functions"
    )
    pdf.multi_cell(
        0,
        6,
        "- Cross-platform: Runs on Windows, macOS, Linux, and other operating systems",
    )
    pdf.multi_cell(
        0, 6, "- Strong Community: Extensive documentation and active community support"
    )
    pdf.ln(5)

    # Data Types
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Python Data Types", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 6, "Python supports various built-in data types:")
    pdf.ln(2)
    pdf.multi_cell(0, 6, "1. Numeric Types: int, float, complex")
    pdf.multi_cell(0, 6, "2. Sequence Types: list, tuple, range, string")
    pdf.multi_cell(0, 6, "3. Mapping Type: dict (dictionary)")
    pdf.multi_cell(0, 6, "4. Set Types: set, frozenset")
    pdf.multi_cell(0, 6, "5. Boolean Type: bool (True, False)")
    pdf.multi_cell(0, 6, "6. None Type: NoneType")
    pdf.ln(5)

    # OOP
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Object-Oriented Programming", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(
        0,
        6,
        "Python supports object-oriented programming (OOP) paradigms. Key concepts include:",
    )
    pdf.ln(2)
    pdf.multi_cell(
        0, 6, "- Classes and Objects: Classes are blueprints for creating objects"
    )
    pdf.multi_cell(
        0,
        6,
        "- Inheritance: Allows a class to inherit attributes and methods from another class",
    )
    pdf.multi_cell(0, 6, "- Encapsulation: Bundling data and methods within a class")
    pdf.multi_cell(
        0,
        6,
        "- Polymorphism: Objects of different classes treated as objects of a common parent class",
    )
    pdf.ln(5)

    # Libraries
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Popular Python Libraries", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(
        0, 6, "Python's ecosystem includes powerful libraries for various domains:"
    )
    pdf.ln(2)
    pdf.multi_cell(0, 6, "- NumPy: Numerical computing and array operations")
    pdf.multi_cell(0, 6, "- Pandas: Data manipulation and analysis")
    pdf.multi_cell(0, 6, "- Matplotlib/Seaborn: Data visualization")
    pdf.multi_cell(0, 6, "- TensorFlow/PyTorch: Deep learning frameworks")
    pdf.multi_cell(0, 6, "- Django/Flask: Web development frameworks")
    pdf.multi_cell(0, 6, "- Scikit-learn: Machine learning algorithms")
    pdf.multi_cell(0, 6, "- Requests: HTTP library for API interactions")

    pdf.output(filename)
    print(f"✓ Created: {filename}")


def create_data_science_pdf():
    """Create a PDF about Data Science"""
    from fpdf import FPDF

    filename = "data/Data_Science_Fundamentals.pdf"
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 24)
    pdf.cell(0, 20, "Data Science Fundamentals", ln=True, align="C")
    pdf.ln(10)

    # What is Data Science
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "What is Data Science?", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(
        0,
        6,
        "Data Science is an interdisciplinary field that uses scientific methods, processes, "
        "algorithms, and systems to extract knowledge and insights from structured and unstructured "
        "data. It combines aspects of statistics, mathematics, programming, and domain expertise "
        "to analyze and interpret complex data sets.",
    )
    pdf.ln(5)

    # Lifecycle
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "The Data Science Lifecycle", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 6, "A typical data science project follows these stages:")
    pdf.ln(2)
    pdf.multi_cell(
        0, 6, "1. Problem Definition: Understanding the business problem and objectives"
    )
    pdf.multi_cell(
        0, 6, "2. Data Collection: Gathering relevant data from various sources"
    )
    pdf.multi_cell(
        0, 6, "3. Data Cleaning: Handling missing values, outliers, and inconsistencies"
    )
    pdf.multi_cell(
        0, 6, "4. Exploratory Data Analysis: Understanding patterns and relationships"
    )
    pdf.multi_cell(
        0,
        6,
        "5. Feature Engineering: Creating new features to improve model performance",
    )
    pdf.multi_cell(
        0, 6, "6. Model Building: Selecting and training appropriate algorithms"
    )
    pdf.multi_cell(
        0, 6, "7. Model Evaluation: Assessing model performance using metrics"
    )
    pdf.multi_cell(0, 6, "8. Deployment: Implementing the model in production")
    pdf.multi_cell(0, 6, "9. Monitoring: Tracking model performance over time")
    pdf.ln(5)

    # Skills
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Essential Skills for Data Scientists", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(
        0, 6, "To succeed in data science, professionals need a combination of skills:"
    )
    pdf.ln(2)
    pdf.multi_cell(0, 6, "- Programming: Proficiency in Python or R")
    pdf.multi_cell(
        0,
        6,
        "- Statistics: Understanding probability, hypothesis testing, and distributions",
    )
    pdf.multi_cell(
        0, 6, "- Machine Learning: Knowledge of various algorithms and when to use them"
    )
    pdf.multi_cell(
        0, 6, "- Data Visualization: Ability to communicate insights effectively"
    )
    pdf.multi_cell(0, 6, "- SQL: Database querying and management")
    pdf.multi_cell(
        0, 6, "- Domain Knowledge: Understanding the specific industry or field"
    )
    pdf.multi_cell(
        0,
        6,
        "- Communication: Explaining technical concepts to non-technical stakeholders",
    )
    pdf.ln(5)

    # Big Data
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Big Data Technologies", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 6, "As data volumes grow, specialized technologies are needed:")
    pdf.ln(2)
    pdf.multi_cell(
        0, 6, "- Apache Hadoop: Distributed storage and processing framework"
    )
    pdf.multi_cell(0, 6, "- Apache Spark: Fast, in-memory data processing engine")
    pdf.multi_cell(0, 6, "- NoSQL Databases: MongoDB, Cassandra for unstructured data")
    pdf.multi_cell(
        0, 6, "- Cloud Platforms: AWS, Google Cloud, Azure for scalable computing"
    )
    pdf.multi_cell(
        0, 6, "- Data Warehouses: Snowflake, Redshift for analytical workloads"
    )
    pdf.ln(5)

    # Career Paths
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Career Paths in Data Science", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 6, "The data science field offers diverse career opportunities:")
    pdf.ln(2)
    pdf.multi_cell(
        0, 6, "- Data Analyst: Focuses on analyzing data and generating reports"
    )
    pdf.multi_cell(
        0, 6, "- Data Scientist: Builds predictive models and extracts insights"
    )
    pdf.multi_cell(0, 6, "- Machine Learning Engineer: Develops and deploys ML systems")
    pdf.multi_cell(
        0, 6, "- Data Engineer: Builds and maintains data pipelines and infrastructure"
    )
    pdf.multi_cell(
        0, 6, "- Business Intelligence Analyst: Creates dashboards and visualizations"
    )
    pdf.multi_cell(0, 6, "- Research Scientist: Conducts advanced research in AI/ML")

    pdf.output(filename)
    print(f"✓ Created: {filename}")


def main():
    """Main function to generate all sample PDFs."""
    print("=" * 60)
    print("📄 Creating Sample PDF Documents")
    print("=" * 60)
    print()

    # Check dependencies
    if not check_dependencies():
        sys.exit(1)

    # Create data directory if it doesn't exist
    os.makedirs("data", exist_ok=True)
    print()

    try:
        print("Generating PDFs...\n")
        create_ai_ml_pdf()
        create_python_programming_pdf()
        create_data_science_pdf()

        print("\n" + "=" * 60)
        print("✅ All sample PDFs created successfully!")
        print("=" * 60)
        print("\nGenerated files:")
        print("  • data/AI_and_Machine_Learning.pdf")
        print("  • data/Python_Programming_Guide.pdf")
        print("  • data/Data_Science_Fundamentals.pdf")
        print("\nYou can now:")
        print("  1. Run the Streamlit UI: streamlit run ui/app.py")
        print("  2. Run the CLI: python -m agent.tools.runner")
        print("  3. Ingest these PDFs and start asking questions!")
        print()

    except Exception as e:
        print(f"\n❌ Error creating PDFs: {e}")
        print("\nTroubleshooting:")
        print("  • Make sure fpdf2 is installed: pip install fpdf2")
        print("  • Check if data/ directory has write permissions")
        sys.exit(1)


if __name__ == "__main__":
    main()
