from lib.db.seed import seed_data
from lib.db.connection import CONN
from lib.models.author import Author
from lib.models.magazine import Magazine
import os

os.system("sqlite3 articles.db < lib/db/schema.sql")
seed_data()

alice = Author.find_by_id(1)
print(alice)
print("Articles by Alice:", alice.articles())
print("Magazines Alice wrote for:", alice.magazines())

mag = Magazine.find_by_id(1)
print(mag)
print("Articles in Mag:", mag.articles())
print("Contributors:", mag.contributors())
print("Titles:", mag.article_titles())