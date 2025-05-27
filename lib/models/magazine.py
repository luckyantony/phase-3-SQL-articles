from lib.db.connection import CURSOR, CONN

class Magazine:
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category

    @classmethod
    def create(cls, name, category):
        CURSOR.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", (name, category))
        CONN.commit()
        return cls(CURSOR.lastrowid, name, category)

    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute("SELECT * FROM magazines WHERE id = ?", (id,))
        row = CURSOR.fetchone()
        if row:
            return cls(*row)
        return None

    def articles(self):
        from lib.models.article import Article
        CURSOR.execute("SELECT * FROM articles WHERE magazine_id = ?", (self.id,))
        return [Article(*row) for row in CURSOR.fetchall()]

    def contributors(self):
        from lib.models.author import Author
        CURSOR.execute('''
            SELECT DISTINCT authors.* FROM authors
            JOIN articles ON articles.author_id = authors.id
            WHERE articles.magazine_id = ?
        ''', (self.id,))
        return [Author(*row) for row in CURSOR.fetchall()]

    def article_titles(self):
        CURSOR.execute("SELECT title FROM articles WHERE magazine_id = ?", (self.id,))
        return [row[0] for row in CURSOR.fetchall()]

    def __repr__(self):
        return f"<Magazine {self.name}>"

    # ✅ Add these two methods to support proper comparison
    def __eq__(self, other):
        return isinstance(other, Magazine) and self.id == other.id

    def __hash__(self):
        return hash(self.id)
