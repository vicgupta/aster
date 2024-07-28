import os, json
from aster.models import OllamaModel, GroqModel, OpenAIModel
from aster.agents import Agent
from aster.db.sqlite3orm import SQLite3ORM
from aster.db.pocketbaseorm import PocketbaseORM
from aster.tools import WebTools

llm = OllamaModel(model="llama3.1")
agent = Agent(llm)
summarizer = Agent(llm, custom_system_prompt="You summarize the text in few paragraphs.")
# response = agent.ask(prompt="why is the sky blue?")
# print(response)

# db = SQLModel(db_name='aster.db')
# db.create_table('users', {'id': 'INTEGER PRIMARY KEY', 'name': 'TEXT', 'age': 'INTEGER'})
# # db.insert('users', {'name': 'John Doe', 'age': 10})
# users = db.select('users', where='age > 20')
# # users = db.select("users", columns=["name", "age"], where="age < 20")
# print(users)

# pb = PocketbaseORM(pb_url=, pb_useremail='', pb_password='', pb_collection=)

search_results = WebTools.get_duckduckgo_search("ollama api", region="us-en", safesearch="on", timeline="w", max_results=5)
# print(search_results)
for item in search_results:
    # print(item['title'], item['href'])
    content_page = WebTools.get_text_from_url(item['href'])
    content_summarizer = summarizer.ask(prompt=content_page)
    print (content_summarizer)
    # print ("-"*120)
    # print (content_page)
    print ("*"*120)
    # print(item['body'])