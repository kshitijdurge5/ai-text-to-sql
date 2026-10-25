import sqlite3
conn = sqlite3.connect("sample.db")
conn.executescript("""
CREATE TABLE IF NOT EXISTS sales (id INTEGER PRIMARY KEY, region TEXT, amount REAL);
DELETE FROM sales;
INSERT INTO sales(region, amount) VALUES ('West',1200),('East',950),('North',1430),('West',500);
""")
conn.commit()
conn.close()
print("Created sample.db")
