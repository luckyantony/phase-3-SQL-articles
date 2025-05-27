from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

print("Seeding test data...")

# Create authors
a1 = Author("Alice")
a1.save()
a2 = Author("Bob")
a2.save()

# Create magazines
m1 = Magazine("Tech Weekly", "Technology")
m1.save()
m2 = Magazine("Health Monthly", "Health")
m2.save()

# Add articles
a1.add_article(m1, "AI and the Future")
a2.add_article(m1, "Robots at Work")
a2.add_article(m2, "Mental Health Awareness")

print("Seeding done.")