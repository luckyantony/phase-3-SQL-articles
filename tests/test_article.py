from lib.models.article import Article
from lib.models.author import Author
from lib.models.magazine import Magazine

def test_article_relationships():
    author = Author.create("Writer A")
    mag = Magazine.create("News", "General")
    article = Article.create("Headline", "News Body", author.id, mag.id)
    assert article.author().id == author.id
    assert article.magazine().id == mag.id