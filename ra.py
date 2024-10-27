from aster.models import OllamaModel
from aster.agents import Agent, ReasoningAgent

llm = OllamaModel(model="llama3.1")
ra = ReasoningAgent(llm, max_tokens=1024)
print (ra.ask("What is the capital of France?"))