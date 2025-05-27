from lib.models.magazine import Magazine
from lib.models.author import Author
from lib.models.article import Article

def test_magazine_articles_titles():
    author = Author.create("Test Author")
    mag = Magazine.create("Sports", "Sports")
    Article.create("Match Day", "Exciting content", author.id, mag.id)
    assert "Match Day" in mag.article_titles()