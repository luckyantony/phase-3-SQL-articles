from lib.db.connection import get_connection
from lib.models.article import Article
from lib.models.author import Author

class Magazine:
    def __init__(self, name, category, id=None):
        self.id = id
        self.name = name
        self.category = category

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", (self.name, self.category))
            self.id = cursor.lastrowid
        else:
            cursor.execute("UPDATE magazines SET name=?, category=? WHERE id=?", (self.name, self.category, self.id))
        conn.commit()
        conn.close()

    def articles(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE magazine_id=?", (self.id,))
        rows = cursor.fetchall()
        return [Article(row['title'], row['author_id'], row['magazine_id'], row['id']) for row in rows]

    def contributors(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
        SELECT DISTINCT a.* FROM authors a
        JOIN articles art ON a.id = art.author_id
        WHERE art.magazine_id = ?
        """, (self.id,))
        rows = cursor.fetchall()
        return [Author(row['name'], row['id']) for row in rows]

    def article_titles(self):
        return [a.title for a in self.articles()]

    def contributing_authors(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
        SELECT author_id, COUNT(*) as count FROM articles
        WHERE magazine_id=?
        GROUP BY author_id HAVING count > 2
        """, (self.id,))
        rows = cursor.fetchall()
        result = []
        for row in rows:
            author_id = row['author_id']
            cursor.execute("SELECT * FROM authors WHERE id=?", (author_id,))
            author_row = cursor.fetchone()
            result.append(Author(author_row['name'], author_row['id']))
        return result