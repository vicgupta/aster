from aster.models import OllamaModel
from aster.agents import Agent

llm = OllamaModel(model="llama3.1")
agent = Agent(llm)
response = agent.ask(prompt="why is the sky blue?")
print(response)
