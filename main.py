import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import sqlite3
import csv
import os

# tkinter p interface  

DB_FILE = "wallet.db"

def init_db():
    with sqlite3.connect(DB_FILE) as conn: # with sqlite3.connect → abre conexão e fecha sozinha no final.
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                type TEXT NOT NULL CHECK(type IN ('receita','despesa')), # só pode ser receita ou depesa
                category TEXT NOT NULL,
                amount REAL NOT NULL,
                bank TEXT,
                asset TEXT
            )
        """)

def add_transaction(date, ttype, category, amount, bank, asset):
    with sqlite3.connect(DB_FILE) as conn:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO transactions (date, type, category, amount, bank, asset) VALUES (?,?,?,?,?,?)",
            (date, ttype, category, amount, bank, asset)
        )
        conn.commit()            
        )
