import sqlite3
import csv

open_csv = open("food.csv")
read_csv = csv.reader(open_csv)
con = sqlite3.connect("db.sqlite3")

cur = con.cursor()

fooddb = "CREATE TABLE IF NOT EXISTS app_sotsu_food(id TEXT, name TEXT, energy INTEGER, protein REAL, lipid REAL, carbo REAL)"
cur.execute(fooddb)

rows = []
for row in read_csv:
    rows.append(row)
    
cur.executemany(
    """INSERT INTO app_sotsu_food VALUES(?,?,?,?,?,?)""",rows
)

con.commit()
open_csv.close()
cur.close()