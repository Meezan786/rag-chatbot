#!/usr/bin/env python3
"""
Simple launcher script for RAG Agent.
Handles path setup and launches the application.
"""

import os
import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.resolve()
sys.path.insert(0, str(project_root))

# Change to project directory
os.chdir(project_root)

# Load environment variables
from dotenv import load_dotenv

load_dotenv()


def main():
    """Main launcher function."""
    print("=" * 60)
    print("🚀 RAG Agent Launcher")
    print("=" * 60)
    print()

    # Check if .env file exists
    env_file = project_root / ".env"
    if not env_file.exists():
        print("❌ Error: .env file not found!")
        print()
        print("Please create a .env file with your OpenAI API key:")
        print('  echo "OPENAI_API_KEY=sk-your-key-here" > .env')
        print()
        print("Or manually create .env file with:")
        print("  OPENAI_API_KEY=sk-your-actual-api-key-here")
        print()
        sys.exit(1)

    # Check if API key is set
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("❌ Error: OPENAI_API_KEY not found in .env file!")
        print()
        print("Please add your OpenAI API key to .env file:")
        print("  OPENAI_API_KEY=sk-your-actual-api-key-here")
        print()
        print("Get your API key from: https://platform.openai.com/api-keys")
        print()
        sys.exit(1)

    if not api_key.startswith("sk-"):
        print("⚠️  Warning: Your API key doesn't look correct (should start with 'sk-')")
        print()
        response = input("Continue anyway? (y/n): ").strip().lower()
        if response != "y":
            print("Exiting...")
            sys.exit(1)
        print()

    print("✅ API key found!")
    print()

    # Check if data directory has PDFs
    data_dir = project_root / "data"
    if data_dir.exists():
        pdf_files = list(data_dir.glob("*.pdf"))
        if len(pdf_files) == 0:
            print("📄 No PDF files found in data/ directory")
            print()
            response = input("Generate sample PDFs? (y/n): ").strip().lower()
            if response == "y":
                print("\n📝 Generating sample PDFs...")
                try:
                    exec(open("create_sample_pdfs_simple.py").read())
                except Exception as e:
                    print(f"❌ Error: {e}")
                    print(
                        "You can generate PDFs later with: python3 create_sample_pdfs_simple.py"
                    )
            print()

    print("Choose how to run:")
    print()
    print("1. 🌐 Streamlit Web UI (Recommended)")
    print("2. 💻 Command Line Interface")
    print("3. ❌ Exit")
    print()

    choice = input("Enter choice (1-3): ").strip()
    print()

    if choice == "1":
        print("🚀 Starting Streamlit UI...")
        print("Opening at http://localhost:8501")
        print()
        print("Press Ctrl+C to stop")
        print()

        import subprocess

        try:
            subprocess.run(["streamlit", "run", "ui/app.py"])
        except KeyboardInterrupt:
            print("\n\n👋 Shutting down...")
        except FileNotFoundError:
            print("❌ Streamlit not found!")
            print("Install it with: pip install streamlit")
            sys.exit(1)

    elif choice == "2":
        print("🚀 Starting CLI...")
        print("Type 'exit' to quit")
        print()

        try:
            from agent.tools.runner import run_agent

            run_agent()
        except ImportError as e:
            print(f"❌ Import error: {e}")
            print("\nTry installing the package:")
            print("  pip install -e .")
            sys.exit(1)
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")

    elif choice == "3":
        print("👋 Goodbye!")
        sys.exit(0)

    else:
        print("❌ Invalid choice")
        sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
        sys.exit(0)
