import sqlite3

DATABASE_NAME = "products.db"


def get_db_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    return connection


def create_tables():
    connection = get_db_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price INTEGER NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def insert_sample_product():
    connection = get_db_connection()

    connection.execute(
        "INSERT OR IGNORE INTO products (id, name, price) VALUES (?, ?, ?)",
        (1, "mobile", 200000)
    )

    connection.execute(
        "INSERT OR IGNORE INTO products (id, name, price) VALUES (?, ?, ?)",
        (2, "TABLETS", 300000)
    )

    connection.commit()
    connection.close()


def get_all_products():
    connection = get_db_connection()

    rows = connection.execute(
        "SELECT * FROM products"
    ).fetchall()

    connection.close()

    return [dict(row) for row in rows]

## create product
def create_product(name: str, price: int):
    connection = get_db_connection()

    cursor = connection.execute(
        "INSERT INTO products (name, price) VALUES (?, ?)",
        (name, price)
    )

    connection.commit()

    product_id = cursor.lastrowid

    connection.close()

    return {
        "id": product_id,
        "name": name,
        "price": price
    }

## get product by id

def get_product_by_id(product_id:int):
    connection = get_db_connection()
    row = connection.execute("SELECT * FROM products WHERE id = ?",(product_id,)).fetchone()
    connection.close()

    if row is None:
        return None

    return dict(row)

# update the old product
def update_product(product_id:int ,name:str , price:int):
    connection = get_db_connection()
    cursor = connection.execute(
        """
        UPDATE products
        SET name = ?, price = ?
        WHERE id = ?
        """,
        (name, price, product_id)
    )
    connection.commit()
    if cursor.rowcount == 0:
        connection.close()
        return None

    row = connection.execute(
        "SELECT * FROM products WHERE id = ?",
        (product_id,)
    ).fetchone()

    connection.close()

    return dict(row)

### delete by id
def delete_product(product_id: int):
    connection = get_db_connection()

    cursor = connection.execute(
        "DELETE FROM products WHERE id = ?",
        (product_id,)
    )

    connection.commit()

    if cursor.rowcount == 0:
        connection.close()
        return False

    connection.close()

    return True



  