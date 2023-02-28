import sqlite3 as sl
import emp as emp

connection = sl.connect('Game')
with connection:
    connection.execute("""
        CREATE TABLE IF NOT EXISTS  games (
            User_id INTEGER,
            score INTEGER,
            time INTEGER
        );
""")

sql = 'INSERT INTO games (User_id, score,time) values(?,?,?)'
data = [
    (1, 200, 100000),
    (1, 300, 110010),
    (2, 500, 100010),
    (1, 400, 201034),
    (3, 100, 200010),
    (2, 600, 210000),
    (2, 300, 210010)

]

with connection:
    connection.executemany(sql, data)


with connection:
    connection.execute("""
        CREATE TABLE IF NOT EXISTS  Users (
            rowid INTEGER,
            name TEXT,
            sex INTEGER,
            old INTEGER,
            score INTEGER
        );
""")

sql = 'INSERT INTO Users (rowid,name,sex,old,score) values(?,?,?,?,?)'
data = [
    (1, "Михаил", 1, 22, 1000),
    (2, "Яна", 2, 24, 830),
    (3, "Федор", 1, 32, 764)
]

with connection:
    connection.executemany(sql, data)
