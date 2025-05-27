from lib.models.article import Article

def test_create_article():
    article = Article.create("Test", "Content", 1, 1)
    assert article.title == "Test"

def test_article_relationships():
    article = Article.create("Linked", "Content", 1, 1)
    assert article.author().name
    assert article.magazine().name