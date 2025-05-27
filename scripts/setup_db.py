import sqlite3
from lib.db.connection import get_connection

with open("lib/db/schema.sql") as f:
    schema_sql = f.read()

conn = get_connection()
cursor = conn.cursor()
cursor.executescript(schema_sql)
conn.commit()
print("Database setup complete.")
conn.close()