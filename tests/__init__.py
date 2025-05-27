import os
import sqlite3

CONN = sqlite3.connect('articles.db')
CURSOR = CONN.cursor()

def run_schema():
    with open('lib/db/schema.sql', 'r') as f:
        CURSOR.executescript(f.read())
    CONN.commit()

run_schema()
