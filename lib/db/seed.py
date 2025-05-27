from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def seed_data():
    author1 = Author.create("Alice Smith")
    author2 = Author.create("Bob Johnson")

    mag1 = Magazine.create("Tech Monthly", "Technology")
    mag2 = Magazine.create("Health Weekly", "Health")

    Article.create("The Rise of AI", "AI content", author1.id, mag1.id)
    Article.create("Staying Fit", "Health content", author2.id, mag2.id)
    Article.create("AI in Medicine", "Combo content", author1.id, mag2.id)