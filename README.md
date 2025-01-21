# AgenticAI Suite

AgenticAI Suite is a Python-based project that implements specialized AI agents to handle dynamic queries across different domains. The suite includes:
- A **Web Search Agent** for retrieving concise information from the web.
- A **Finance Agent** for fetching financial data, including stock prices and analyst recommendations.
- An **Image Analysis Agent** for analyzing images and providing contextual information.

The project demonstrates the potential of modular AI systems in automating tasks and responding to user queries efficiently.

---

## Features
- **Dynamic User Input**: Allows users to interact with agents in real time.
- **Web Search**: Retrieves relevant web results using DuckDuckGo.
- **Financial Insights**: Provides real-time stock prices, company news, and analyst recommendations via YFinance.
- **Image Analysis**: Analyzes images and retrieves contextual information using Groq's image models.
- **Modular Design**: Each agent is independent, making the system extensible for new domains.


---

## Installation

### Prerequisites
- Python 3.12 or higher
- `pip` (Python package installer)
- A GitHub account for code cloning

### Steps to Set Up
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/disha-karmakar/AgenticAI.git
   cd AgenticAI
2. **Set Up a Virtual Environment:**

    ```bash

    python -m venv .venv
    source .venv/bin/activate    # For Windows: .venv\Scripts\activate
3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
4. **Configure Environment Variables:**

- Create a .env file in the project directory:
    ```bash
    touch .env
- Add the required environment variables:
    ```bash
    # Replace with your own values if necessary
    DUCKDUCKGO_API_KEY=
---

## Usage
**Running Agents**
1. **Web Search Agent:**
    ```
    python search_agent.py
**Example Query:** "What is the tallest mountain in the world?"

2. **Finance Agent:**
    ```
    python finance_agent.py
**Example Query:** "What is the current stock price of Tesla (TSLA)?"

3. **Image Analysis Agent:**
    ```
    python image_agent.py
**Example Query:**
- **Image URL:** https://upload.wikimedia.org/wikipedia/commons/d/d0/Taj-Mahal-Agra.jpg
- **Query:** "Describe the architectural significance of this monument."
---
## Example Outputs
1. **Web Search Agent**
**Query**: "When was the Eiffel Tower built?"
**Response**:
    ```
    The Eiffel Tower was built in 1887 and completed in 1889. It is located in Paris, France.

2. **Finance Agent**
**Query**: "Get the current stock price and latest news for Apple (AAPL)."
**Response**:
    ```
    Stock Price: $175.35
    Analyst Recommendations:
   - Buy: 10
   - Hold: 5
   - Sell: 2
**Latest News:** Apple announces a new product lineup for Q4 2024.

3. **Image Analysis Agent**
**Query**:
**Image URL**: https://upload.wikimedia.org/wikipedia/commons/d/d0/Taj-Mahal-Agra.jpg
**Text**: "Describe the architectural significance of this monument."
**Response**:
    ```
    The image shows the Taj Mahal, a UNESCO World Heritage Site in Agra, India. Built by Emperor Shah Jahan in memory of Mumtaz Mahal, it is renowned for its white marble architecture, intricate carvings, and symmetrical gardens.
---
## Limitations
- **Rate Limits:** Web Search and Financial Data tools are subject to API rate limits.
- **Image Analysis:** Requires a valid image URL and is limited by the capabilities of the Groq model.
---
## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.


