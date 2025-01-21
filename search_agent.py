from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
import groq

load_dotenv()

SimpleSearchAgent = Agent(
    name="Web Agent",
    description="This agent searches content from the web",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions="Always include the sources",
)

if __name__ == "__main__":
    try:
        query = input("Enter your query for the Web Search Agent: ")
        SimpleSearchAgent.print_response(
            message=query, stream=True
        )
    except groq.APIError as e:
        print(f"Error: {e}. Please try rephrasing your query or check your API connection.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
