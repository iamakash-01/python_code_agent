import os
from dotenv import load_dotenv
from groq import Groq
from agno.agent import Agent, RunResponse
from agno.models.groq import Groq
from agno.tools.python import PythonTools

# load the api_key
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# AI agent
code_agent = Agent(
    name = "AIcodeAgent",
    model = Groq(id = "llama-3.3-70b-versatile"),
    description = "Code agent made by Akash a.k.a Ultron",
    tools = [PythonTools()],
    show_tool_calls = True,
    debug_mode = True,
    markdown = True
)

# response from agent
def generate_python_code():
    user_input = input("Provide the python question: ")
    print("\nGenerating code based on your question") 
    code_response = code_agent.print_response(user_input, stream = True)

    return code_response

# main func
if __name__ == "__main__":
    generate_python_code()
