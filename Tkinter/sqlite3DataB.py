import sqlite3

# Connect to Database
conn = sqlite3.connect("sqllite.db")
# Create cursor object
cur = conn.cursor()
# write SQL query
cur.execute("CREATE TABLE Product (item TEXT, quantity INTEGER, price REAL)")
# commit changes
conn.commit()
#close database
conn.close()

