# Financial-Agent-using-Agentic-AI

This project is a Streamlit-based web application that integrates multiple AI agents to provide financial insights and web search capabilities. The application uses the Groq model for AI processing, along with tools like `YFinanceTools` for financial data and `DuckDuckGo` for web searches. Users can ask questions, and the application will provide responses in real-time.

---

## Table of Contents
1. [Description](#description)
2. [Tech Stack](#tech-stack)
3. [Installation](#installation)
6. [Usage](#usage)
7. [Contributing](#contributing)

---

## Description

This application leverages the power of AI agents to:
- Fetch financial data (e.g., stock prices, analyst recommendations) using `YFinanceTools`.
- Perform web searches using `DuckDuckGo`.
- Provide real-time responses to user queries using the Groq model (`llama-3.3-70b-versatile`).

The application is built using **Streamlit**, making it easy to deploy and interact with in a web browser.

---

## Tech Stack

- **Streamlit**: A Python library for building interactive web applications.
- **Groq**: A high-performance AI model used for generating responses.
- **YFinanceTools**: A tool for fetching financial data (e.g., stock prices, analyst recommendations).
- **DuckDuckGo**: A tool for performing web searches.
- **Python**: The primary programming language used for this project.
- **Conda**: A package and environment management system for Python.

---

## Installation

### Prerequisites
1. **Python 3.8+**: Ensure Python is installed on your system.
2. **Conda**: Install Conda for managing virtual environments.

### Steps
1. Clone the repository:
```bash
  git clone https://github.com/Srijansarkar17/Financial-Agent-using-Agentic-AI.git
  
  cd Financial-Agent-using-Agentic-AI
```
2. Install the required dependencies
```bash
  pip install -r requirements.txt
```
3. Set up environment variables:
      Create a .env file in the root directory.

      Add your OpenAI API key and Groq API key (if required) to the .env file:
```bash
  OPENAI_API_KEY=your_openai_api_key
  GROQ_API_KEY=your_groq_api_key
```
4. Creating and activating a virtual environment
```bash
  conda create -p venv python==3.12 -y
  conda activate venv/
```
## Usage
Ask Financial Questions:

Example: "What is the stock price of NVDA?"

The application will fetch the latest stock price and display it in a table.

Search the Web:

Example: "What is the latest news about NVDA?"

The application will perform a web search and provide the latest news with sources.

Combine Financial and Web Data:

Example: "Summarize analyst recommendations and share the latest news for NVDA."

The application will provide a combined response with financial data and web search results.

## Contributing
- Contributions are welcome! If you'd like to contribute, please follow these steps:

- Fork the repository.

- Create a new branch for your feature or bugfix.

- Commit your changes.

- Push your branch and submit a pull request

