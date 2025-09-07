import sqlite3
import random

def main():
    conn = sqlite3.connect("shop.db")
    conn.execute("PRAGMA foreign_keys = ON;")
    cur = conn.cursor()

    # Recreate schema
    cur.executescript("""
    ---DROP TABLE IF EXISTS orders;
    ---DROP TABLE IF EXISTS products;

    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        price NUMERIC NOT NULL CHECK (price > 0),
        stock INTEGER NOT NULL CHECK (stock >= 0)
    );

    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL CHECK (quantity >= 0),
        total_price NUMERIC NOT NULL CHECK (total_price >= 0),
        order_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (product_id) REFERENCES products(id)
            ON UPDATE CASCADE ON DELETE RESTRICT
    );
    """)

    # # Seed products (so SELECT/FOREIGN KEY don’t fail)
    # cur.executemany(
    #     "INSERT OR IGNORE INTO products (name, price, stock) VALUES (?, ?, ?)",
    #     [
    #         ("iphone 11", 400, 10),
    #         ("iphone 12", 500, 10),
    #         ("iphone 13", 600, 10),
    #         ("iphone 14", 700, 10),
    #     ]
    # )
    #
    # # Choose a valid product id
    # model_id = random.randint(1, 4)
    # cur.execute("SELECT price FROM products WHERE id = ?", (model_id,))
    # product_price = cur.fetchone()[0]
    # quantity = random.randint(1, 3)
    # total_price = product_price * quantity
    #
    # # NOTE: column name is product_id (not products_id)
    # cur.execute("INSERT INTO orders (product_id, quantity, total_price) VALUES (?, ?, ?)",
    #             (model_id, quantity, total_price))
    #
    # print("PRoducts:")
    # cur.execute("SELECT * FROM products;")
    # for row in cur.fetchall():
    #     print(row)
    #
    # cur.execute("""
    #     SELECT products.name,orders.quantity,orders.total_price,orders.order_date
    #     FROM orders
    #     JOIN products ON orders.product_id = products.id
    #     ORDER BY orders.id;
    # """)
    # print("\nOrders")
    # orders = cur.fetchall()
    # for order in orders:
    #     print(order)
    #
    # print("\nProducts with name LIKE %4 : ")
    # cur.execute("SELECT * FROM products WHERE name LIKE '%4';")
    # for row in cur.fetchall():
    #     print(row)
    #
    # print("\n\tOrders with price over 1000$")
    # cur.execute("SELECT * FROM orders WHERE total_price >= 1000 ORDER BY  total_price DESC;")
    # for row in cur.fetchall():
    #     print(row)
    #
    # print("\n\tProducts with price over 1000$")
    # cur.execute("SELECT * FROM products WHERE price >= 1000;")
    # for row in cur.fetchall():
    #     print(row)


    print('count()')
    cur.execute("SELECT COUNT(DISTINCT product_id) AS unique_product FROM orders")
    for row in cur.fetchall():
        print(row)

    print("Sum() product - ")
    cur.execute("SELECT SUM(total_price) AS total_sales FROM orders")
    for row in cur.fetchall():
        print(row)

    print("Average price products - ")
    cur.execute("SELECT AVG(price) AS average_price FROM products")
    for row in cur.fetchall():
        print(row)

    print("Average price of orders - ")
    cur.execute("SELECT AVG(total_price) AS average_price FROM orders")
    for row in cur.fetchall():
        print(row)

    print("max price of orders - ")
    cur.execute("SELECT MAX(total_price) AS max_price FROM orders")
    for row in cur.fetchall():
        print(row)

    print("max price of product - ")
    cur.execute("SELECT MAX(price) AS max_price FROM products")
    for row in cur.fetchall():
        print(row)

    print("sum of price of products - ")
    cur.execute("SELECT product_id, SUM(total_price) AS total_price "
                "FROM orders "
                "GROUP BY product_id"
               )
    for row in cur.fetchall():
        print(row)

    cur.execute("CREATE TABLE IF NOT EXISTS users("
                "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                "name TEXT NOT NULL,"
                "email TEXT UNIQUE NOT NULL);")

    # cur.execute("""ALTER TABLE orders ADD COLUMN user_id INTEGER REFERENCES users(id) ON DELETE CASCADE;""")
    


    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()
