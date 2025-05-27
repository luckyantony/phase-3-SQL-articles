from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.db.seed import seed_data
import os

os.system("sqlite3 articles.db < lib/db/schema.sql")
seed_data()

alice = Author.find_by_id(1)
print(alice)
print("Articles by Alice:", alice.articles())
print("Magazines Alice wrote for:", alice.magazines())

tech = Magazine.find_by_id(1)
print(tech)
print("Tech Articles:", tech.articles())
print("Tech Contributors:", tech.contributors())
print("Tech Titles:", tech.article_titles())

# --- scripts/setup_db.py ---
import os
os.system("sqlite3 articles.db < lib/db/schema.sql")

# --- scripts/run_queries.py ---
from lib.db.seed import seed_data
seed_data()