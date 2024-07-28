# Aster - AI Agentic Framework for Beginners
Aster (or aster) is a simple AI agentic framework for Beginners.  You can get started with copy/paste a few lines of code.

Written in python, a beginner can use most models like Ollama, OpenAI, Groq, etc. to build agents and systems with it.

### Simple way to start with Aster
``` python
from aster.models import OllamaModel
from aster.agents import Agent

llm = OllamaModel(model="llama3")
agent = Agent(llm)
response = agent.ask(prompt="why is the sky blue?")
print(response)
```
### Giving a personality to Agent by adding custom system prompt
``` python
from aster.models import OllamaModel
from aster.agents import Agent

llm = OllamaModel(model="llama3")
agent = Agent(llm, custom_system_prompt="You are a Pirate named Matey.")
response = agent.ask(prompt="why is the sky blue?")
print(response)
```
### Add options to Agent
``` python
from aster.models import OllamaModel, OpenAIModel
from aster.agents import Agent

llm_llama3 = OllamaModel(model="llama3")
llm_gpt4om = OpenAIModel(model="gpt-4o-mini", api_key="sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXX")
agent = Agent(llm_llama3, custom_system_prompt="You are a Pirate named Matey.")
summarizer = Agent(llm_gpt4om, custom_system_prompt="You summarize the text in few paragraphs.")
response = agent.ask(prompt="why is the sky blue?")
print(response)
```
### Duck Duck Go Search (used as a tool to agent)
``` python
search_results = WebTools.get_duckduckgo_search("chatgpt", region="us-en", safesearch="on", timeline="w", max_results=5)
for item in search_results:
    print(item['title'], item['href'])
    print(item['body'])
```

### Summarize Duck Duck Go Search pages one by one
``` python
from aster.models import OllamaModel
from aster.agents import Agent
from aster.tools import WebTools

llm = OllamaModel(model="llama3")
summarizer = Agent(llm_gpt4om, custom_system_prompt="You summarize the text in few paragraphs.")

search_results = WebTools.get_duckduckgo_search("chatgpt", region="us-en", safesearch="on", timeline="w", max_results=5)
print(search_results)
for item in search_results:
    print(item['title'], item['href'], item['body'])
    content_page = WebTools.get_text_from_url(item['href'])
    content_summarizer = summarizer.ask(prompt=content_page)
    print (content_summarizer)
    print ("*"*120)
```