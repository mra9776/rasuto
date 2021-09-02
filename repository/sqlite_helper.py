import logging
import sqlite3
from sqlite3.dbapi2 import Row
from typing import List

logger = logging.getLogger(__name__)
conn = None


def init_connection():
    global conn
    if conn is None:
        conn = sqlite3.connect(database='db.sqlite',
                               detect_types=sqlite3.PARSE_COLNAMES)
        conn.row_factory = Row

def execute(sql: str) -> List[Row]:
    cur = conn.cursor()
    result = cur.execute(sql)
    return result.fetchall()


def commit_a_row(sql: str, data):
    cur = conn.cursor()
    result = cur.execute(sql, [data])
    conn.commit()
    return result


def init_db():
    cur = conn.cursor()
    cur.executescript("""
    create table if not exists users (
        url TEXT, 
        port TEXT, 
        protocol TEXT, 
        is_active INTEGER(1)
    );
    """)
    conn.commit()
