from aster.models import OllamaModel
from aster.agents import Agent
from aster.db.sqlite3orm import SQLite3ORM

llm = OllamaModel(model="llama3.1")
agent = Agent(llm)

db = SQLite3ORM(db_name='aster.db')
db.create_table('users', {'id': 'INTEGER PRIMARY KEY', 'name': 'TEXT', 'age': 'INTEGER'})
db.insert('users', {'name': 'John Doe', 'age': 10})
users_above20 = db.select('users', where='age > 20')
users_below20 = db.select("users", columns=["name", "age"], where="age < 20")
print(users_below20)

