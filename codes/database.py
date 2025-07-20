import sqlite3
import os
import sys

if getattr(sys, 'frozen', False):
    BASE_DIR = sys._MEIPASS
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DB_PATH = os.path.join(BASE_DIR, "cyber_raid.db")

def initialize_db():
<<<<<<< HEAD
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            time REAL,
            score INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def save_score(time, score):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO scores (time, score) VALUES (?, ?)', (time, score))
    conn.commit()
    conn.close()

def get_top_scores(limit=5):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT score, time FROM scores ORDER BY score DESC, time DESC LIMIT ?', (limit,))
    results = cursor.fetchall()
    conn.close()
=======
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS scores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                time REAL,
                score INTEGER
            )
        ''')
        conn.commit()

def save_score(time, score):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO scores (time, score) VALUES (?, ?)', (time, score))
        conn.commit()

def get_top_scores(limit=5):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT score, time FROM scores ORDER BY score DESC, time ASC LIMIT ?', (limit,))
        results = cursor.fetchall()
>>>>>>> 958f78a (Code and executable updated)
    return results
