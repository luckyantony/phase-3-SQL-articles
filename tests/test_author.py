from lib.models.author import Author
from lib.models.article import Article
from lib.models.magazine import Magazine

def test_author_articles():
    author = Author.create("John Doe")
    mag = Magazine.create("Science Today", "Science")
    Article.create("Space", "Content", author.id, mag.id)
    assert len(author.articles()) == 1

def test_author_magazines():
    author = Author.create("Jane Doe")
    mag = Magazine.create("Tech World", "Tech")
    Article.create("Quantum", "Quantum Content", author.id, mag.id)
    assert mag in author.magazines()