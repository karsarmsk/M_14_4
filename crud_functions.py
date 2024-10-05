import sqlite3

# connection = sqlite3.connect("Products.db")
# cursor = connection.cursor()

def initiate_db():
    connection = sqlite3.connect("Products.db")
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INT,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL
    )
    ''')
    for i in range(1, 5):
        cursor.execute(" INSERT INTO Users (id, title, description, price) VALUES (?, ?, ?, ?)",
                       (i,f"Product{i}", f"описание {i}", f"{i * 100}"))
    connection.commit()
    connection.close()

def get_all_products():
    connection = sqlite3.connect("Products.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Users")
    all_product = cursor.fetchall()
    connection.commit()
    connection.close()
    return all_product

# connection.commit()
# connection.close()
