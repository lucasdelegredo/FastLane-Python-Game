#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3

class DBProxy:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection = sqlite3.connect(f"{self.db_name}.db")
        self.cursor = self.connection.cursor()
        
        # Cria a tabela se ela não existir
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS scoreboard (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                score INTEGER NOT NULL,
                date TEXT NOT NULL
            )
        ''')
        self.connection.commit()
        # Apenas para teste inicial:
        self.save({'name': 'TEST', 'score': 100, 'date': '21/03/2024'})

    def save(self, data: dict):
        """Salva um novo recorde no banco"""
        query = "INSERT INTO scoreboard (name, score, date) VALUES (?, ?, ?)"
        values = (data['name'], data['score'], data['date'])
        self.cursor.execute(query, values)
        self.connection.commit()

    def retrieve_top10(self):
        """Busca os 10 melhores resultados em ordem decrescente"""
        query = "SELECT name, score, date FROM scoreboard ORDER BY score DESC LIMIT 10"
        return self.cursor.execute(query).fetchall()

    def close(self):
        self.connection.close()