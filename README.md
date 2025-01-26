# Financial-Agent-using-Agentic-AI

This project is a Streamlit-based web application that integrates multiple AI agents to provide financial insights and web search capabilities. The application uses the Groq model for AI processing, along with tools like `YFinanceTools` for financial data and `DuckDuckGo` for web searches. Users can ask questions, and the application will provide responses in real-time.

---

## Table of Contents
1. [Description](#description)
2. [Tech Stack](#tech-stack)
3. [Installation](#installation)
4. [Running the Application](#running-the-application)
5. [Creating a Virtual Environment with Conda](#creating-a-virtual-environment-with-conda)
6. [Usage](#usage)
7. [Contributing](#contributing)
8. [License](#license)

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
   git clone https://github.com/your-username/multi-ai-financial-agent.git
   cd multi-ai-financial-agent
