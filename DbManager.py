import sqlite3

class DBManager:
    def __init__(self, db_name="game.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS scores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                pontuacao INTEGER NOT NULL
            )
        """)
        self.conn.commit()

    def insert_score(self, nome, pontuacao):
        self.cursor.execute("INSERT INTO scores (nome, pontuacao) VALUES (?, ?)", (nome, pontuacao))
        self.conn.commit()

    def get_top_scores(self, limit=10):
        self.cursor.execute("SELECT nome, pontuacao FROM scores ORDER BY pontuacao DESC LIMIT ?", (limit,))
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()
