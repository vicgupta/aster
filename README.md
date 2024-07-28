# aster


### Simple Example - Easiest way to run Aster
``` python
from aster.models import OllamaModel
from aster.agents import Agent

llm = OllamaModel(model="llama3")
agent = Agent(llm)
response = agent.ask(prompt="why is the sky blue?")
print(response)
```
### Simple Example - Giving a personality to Agent by adding custom system prompt
``` python
from aster.models import OllamaModel
from aster.agents import Agent

llm = OllamaModel(model="llama3")
agent = Agent(llm, custom_system_prompt="You are a Pirate named Matey.")
response = agent.ask(prompt="why is the sky blue?")
print(response)

