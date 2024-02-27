import sqlite3

class Database:
    def __init__(self, nome):
        self.nome = nome
        self.conn = sqlite3.connect(nome)
        