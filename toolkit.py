import sqlite3 as db


def get_tickers() -> list:
    conn = db.connect('CapstoneDB.sqlite')
    conn.row_factory = lambda cursor, row: row[0]
    c = conn.cursor()
    list_of_tickers = c.execute('SELECT stock_ticker FROM main_table').fetchall()
    conn.close()
    return list_of_tickers
