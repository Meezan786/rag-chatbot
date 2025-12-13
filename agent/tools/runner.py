# agent/runner.py
import json
import os
import sys
import time
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

# Load environment variables BEFORE importing OpenAI
from dotenv import load_dotenv

load_dotenv()

from openai import OpenAI

from agent.agent_config import create_rag_agent
from agent.tools.fn_ingest import fn_ingest
from agent.tools.fn_retrieve import fn_retrieve


def run_agent():
    # Check if API key is set
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Error: OPENAI_API_KEY not found in environment variables!")
        print("\nPlease create a .env file in the project root with:")
        print("  OPENAI_API_KEY=your_key_here")
        print("\nOr set it as an environment variable:")
        print("  export OPENAI_API_KEY=your_key_here")
        sys.exit(1)

    client = OpenAI()
    agent = create_rag_agent()

    print("Agent Ready 🚀")

    thread = client.beta.threads.create()  # conversation thread

    while True:
        user_msg = input("You: ")

        if user_msg.lower() in ["exit", "quit", "bye"]:
            print("Goodbye!")
            break

        client.beta.threads.messages.create(
            thread_id=thread.id, role="user", content=user_msg
        )

        run = client.beta.threads.runs.create(
            thread_id=thread.id, assistant_id=agent.id
        )

        # Poll for response
        while True:
            status = client.beta.threads.runs.retrieve(
                thread_id=thread.id, run_id=run.id
            )

            if status.status == "completed":
                break
            elif status.status == "requires_action":
                tool_outputs = []
                for tool_call in status.required_action.submit_tool_outputs.tool_calls:
                    name = tool_call.function.name
                    args = json.loads(tool_call.function.arguments)

                    print(f"🔧 Calling tool: {name}")

                    if name == "fn_ingest":
                        result = fn_ingest(**args)
                    elif name == "fn_retrieve":
                        result = fn_retrieve(**args)
                    else:
                        result = {"error": "Unknown tool"}

                    tool_outputs.append(
                        {"tool_call_id": tool_call.id, "output": json.dumps(result)}
                    )

                client.beta.threads.runs.submit_tool_outputs(
                    thread_id=thread.id, run_id=run.id, tool_outputs=tool_outputs
                )
            elif status.status == "failed":
                print("❌ Run failed:", status.last_error)
                break

            time.sleep(0.5)

        # Print final response
        messages = client.beta.threads.messages.list(thread_id=thread.id)
        print("Bot:", messages.data[0].content[0].text.value)
        print()


if __name__ == "__main__":
    run_agent()
