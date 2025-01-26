import streamlit as st
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Web Search Agent
web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for the information",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources", "Use the latest news source"],
    show_tool_calls=True,
    markdown=True
)

# Financial Agent
finance_agent = Agent(
    name="finance AI Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True
)

# Multi-AI Agent
multi_ai_agent = Agent(
    team=[web_search_agent, finance_agent],
    instructions=["Always include sources", "Use the latest news source", "Use tables to display the data"],
    show_tool_calls=True,
    markdown=True
)

# Streamlit App
st.title("Multi-AI Financial Agent with Streamlit")

# User input
user_input = st.text_input("Ask a question:")

if user_input:
    # Get response from the multi_ai_agent
    response_generator = multi_ai_agent.run(user_input, stream=True)
    
    # Display the response incrementally
    st.write("### Response:")
    response_container = st.empty()  # Create an empty container to update the response dynamically
    full_response = ""

    for chunk in response_generator:
        # Extract the string content from the RunResponse object
        chunk_content = chunk.content if hasattr(chunk, 'content') else str(chunk)
        full_response += chunk_content  # Append each chunk to the full response
        response_container.markdown(full_response)  # Update the container with the latest response