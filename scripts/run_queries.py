from lib.db.seed import seed_data
from lib.models.author import Author
from lib.models.magazine import Magazine

seed_data()
print("Seeded Database")

print(Author.find_by_id(1))
print(Magazine.find_by_id(1).article_titles())