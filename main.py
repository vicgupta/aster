import os, json
from aster.models import OllamaModel, GroqModel, OpenAIModel
from aster.agents import Agent
from aster.sqlite3orm import SQLModel
from aster.pockbaseorm import PocketbaseORM

# llm = OllamaModel(model="gemma2")
# agent = Agent(llm, custom_system_prompt="You are a Business Analyst.", format="json")
# response = agent.ask(prompt=question_prompts)
# print(response)

# db = SQLModel(db_name='aster.db')
# db.create_table('users', {'id': 'INTEGER PRIMARY KEY', 'name': 'TEXT', 'age': 'INTEGER'})
# # db.insert('users', {'name': 'John Doe', 'age': 10})
# users = db.select('users', where='age > 20')
# # users = db.select("users", columns=["name", "age"], where="age < 20")
# print(users)

# pb = PocketbaseORM(pb_url=, pb_useremail='', pb_password='', pb_collection=)