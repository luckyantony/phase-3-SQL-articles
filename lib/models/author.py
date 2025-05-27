from lib.db.connection import CURSOR, CONN

class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @classmethod
    def create(cls, name):
        CURSOR.execute("INSERT INTO authors (name) VALUES (?)", (name,))
        CONN.commit()
        return cls(CURSOR.lastrowid, name)

    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute("SELECT * FROM authors WHERE id = ?", (id,))
        row = CURSOR.fetchone()
        if row:
            return cls(*row)
        return None

    def articles(self):
        from lib.models.article import Article
        return Article.find_by_author_id(self.id)

    def magazines(self):
        from lib.models.magazine import Magazine
        CURSOR.execute('''
            SELECT DISTINCT magazines.* FROM magazines
            JOIN articles ON articles.magazine_id = magazines.id
            WHERE articles.author_id = ?
        ''', (self.id,))
        return [Magazine(*row) for row in CURSOR.fetchall()]

    def __repr__(self):
        return f"<Author {self.name}>"