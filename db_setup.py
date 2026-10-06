import sqlite3

conn = sqlite3.connect("gfc.db")
cur = conn.cursor()
cur.execute("PRAGMA foreign_keys = ON")

cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS diets(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS user_diets(
    user_id INTEGER NOT NULL,
    diet_id INTEGER NOT NULL,
    PRIMARY KEY (user_id, diet_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (diet_id) REFERENCES diets(id)
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS stores(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    location TEXT NOT NULL
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS items(
    id INTEGER PRIMARY KEY,
    brand TEXT NOT NULL,
    item TEXT NOT NULL
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS item_diets(
    item_id INTEGER NOT NULL, 
    diet_id INTEGER NOT NULL,
    PRIMARY KEY (item_id, diet_id),
    FOREIGN KEY (item_id) REFERENCES items(id),
    FOREIGN KEY (diet_id) REFERENCES diets(id)
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS store_items(
    store_id INTEGER NOT NULL,
    item_id INTEGER NOT NULL,
    PRIMARY KEY (store_id, item_id),
    FOREIGN KEY (store_id) REFERENCES stores(id),
    FOREIGN KEY (item_id) REFERENCES items(id)
    )
""")

conn.commit()
conn.close()