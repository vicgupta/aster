from aster.models import OllamaModel
from aster.agents import Agent

llm = OllamaModel(model="llama3.1")
agent = Agent(llm, max_tokens=2048)
response = agent.ask(prompt="Today is Monday")
response = agent.ask(prompt="what is the capital of USA?")
response = agent.ask(prompt="what was yesterday?")
print(response)
