import sqlite3

def create_table():
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

def insert(item, quantity, price):
    conn = sqlite3.connect("sqllite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO Product VALUES (?, ?, ?)", (item, quantity, price))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("sqllite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Product")
    rows = cur.fetchall()
    conn.close()
    return rows   #rows is returned as python list

def delete(item):
    conn = sqlite3.connect("sqllite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM Product WHERE item=?", (item,))
    conn.commit()
    conn.close()

def update(quantity, price, item):
    conn = sqlite3.connect("sqllite.db")
    cur = conn.cursor()
    cur.execute("UPDATE Product SET quantity=?, price=? WHERE item=?", (quantity, price, item))
    conn.commit()
    conn.close()

#insert('Mango', 10, 11.5)
#insert('Orange', 15, 11.5)

update(100, 550, "Mango") # Sequence must be maintained

#delete("Mango")
print(view())
