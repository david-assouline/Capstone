import sqlite3
import pandas as pd

table = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
df = table[0]

conn = sqlite3.connect("CapstoneDB.sqlite")
cursor = conn.cursor()
cursor.execute("DELETE FROM main_table")

for i in range(500):
    cursor.execute("INSERT INTO main_table(stock_ticker, stock_name) VALUES (?,?)", (df['Symbol'][i], df['Security'][i]))

conn.commit()
conn.close()


