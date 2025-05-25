from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

print("-- Debug session starting --")

a1 = Author("Test Author")
a1.save()

m1 = Magazine("Test Mag", "Science")
m1.save()

article = a1.add_article(m1, "Exploring Stars")
print("Added article:", article.title)

print("Author's magazines:", [m.name for m in a1.magazines()])
print("Magazine contributors:", [a.name for a in m1.contributors()])