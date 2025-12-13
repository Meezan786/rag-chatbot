import os
import sys
import time
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Load environment variables BEFORE importing OpenAI
from dotenv import load_dotenv

load_dotenv()

import streamlit as st
from openai import OpenAI

from agent.agent_config import create_rag_agent, get_rag_tools, get_rag_instructions

st.title("RAG Chatbot using OpenAI Responses API")

# Check if API key is set
if not os.getenv("OPENAI_API_KEY"):
    st.error("⚠️ OPENAI_API_KEY not found in environment variables!")
    st.info(
        "Please create a .env file in the project root with:\nOPENAI_API_KEY=your_key_here"
    )
    st.stop()

client = OpenAI()

# Initialize session state
if "agent_config" not in st.session_state:
    st.session_state.agent_config = create_rag_agent()
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if query := st.chat_input("Ask a question:"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)

    # Prepare messages for the API
    api_messages = [{"role": "system", "content": st.session_state.agent_config["instructions"]}]
    api_messages.extend(st.session_state.messages)

    # Create response with tools using Chat Completions API
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = client.chat.completions.create(
                    model=st.session_state.agent_config["model"],
                    messages=api_messages,
                    tools=st.session_state.agent_config["tools"],
                    tool_choice="auto"
                )

                # Handle tool calls if any
                message = response.choices[0].message
                answer = message.content or ""

                tool_calls = message.tool_calls or []
                if tool_calls:
                    # Execute tool calls
                    api_messages.append({
                        "role": "assistant",
                        "content": answer,
                        "tool_calls": [
                            {
                                "id": tc.id,
                                "type": tc.type,
                                "function": {
                                    "name": tc.function.name,
                                    "arguments": tc.function.arguments
                                }
                            } for tc in tool_calls
                        ]
                    })

                    for tool_call in tool_calls:
                        function_name = tool_call.function.name
                        arguments = tool_call.function.arguments

                        # Import and execute the function
                        import json
                        from agent.tools.fn_ingest import fn_ingest
                        from agent.tools.fn_retrieve import fn_retrieve

                        args = json.loads(arguments)

                        if function_name == "fn_ingest":
                            result = fn_ingest(**args)
                        elif function_name == "fn_retrieve":
                            result = fn_retrieve(**args)
                        else:
                            result = {"error": "Unknown function"}

                        api_messages.append({
                            "role": "tool",
                            "tool_call_id": tool_call.id,
                            "content": json.dumps(result)
                        })

                    # Create follow-up response
                    follow_up = client.chat.completions.create(
                        model=st.session_state.agent_config["model"],
                        messages=api_messages,
                        tools=st.session_state.agent_config["tools"],
                        tool_choice="auto"
                    )

                    answer = follow_up.choices[0].message.content or "I couldn't generate a response."

            except Exception as e:
                answer = f"Error: {str(e)}"

        st.markdown(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})
