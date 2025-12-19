import sqlite3
import random

DB_NAME = "support.db"

def get_connection():
    return sqlite3.connect(DB_NAME, check_same_thread=False)

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS support_tickets (
            ticket_id INTEGER PRIMARY KEY,
            issue TEXT,
            status TEXT
        )
    """)
    conn.commit()
    conn.close()

def create_ticket(issue):
    conn = get_connection()
    cur = conn.cursor()
    ticket_id = random.randint(100000, 999999)
    cur.execute(
        "INSERT INTO support_tickets VALUES (?, ?, ?)",
        (ticket_id, issue, "Unresolved")
    )
    conn.commit()
    conn.close()
    return ticket_id

def get_ticket_status(ticket_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT status FROM support_tickets WHERE ticket_id=?",
        (ticket_id,)
    )
    row = cur.fetchone()
    conn.close()
    return row[0] if row else None

def get_ticket_count():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM support_tickets")
    count = cur.fetchone()[0]
    conn.close()
    return count
