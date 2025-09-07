import sqlite3

BASE_DDL = """
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
"""

def main():
    with sqlite3.connect("shop.db", timeout=30) as conn:
        conn.execute("PRAGMA foreign_keys = ON;")
        conn.execute("PRAGMA busy_timeout = 5000;")
        conn.execute("PRAGMA journal_mode = WAL;")

        # 1) Ensure base tables exist
        conn.executescript(BASE_DDL)

        # 2) Build ALTERs only if needed (no IF NOT EXISTS -> max compatibility)
        cols = [r[1] for r in conn.execute("PRAGMA table_info(products)")]
        alter_sql = ""
        if "description" not in cols:
            alter_sql += "ALTER TABLE products ADD COLUMN description TEXT;\n"
        if "quantity_in_stock" not in cols and "stock" in cols:
            alter_sql += "ALTER TABLE products RENAME COLUMN stock TO quantity_in_stock;\n"
        if alter_sql:
            conn.executescript(alter_sql)

        # 3) Insert sample products (works whether column was renamed or not)
        cols = [r[1] for r in conn.execute("PRAGMA table_info(products)")]
        stock_col = "quantity_in_stock" if "quantity_in_stock" in cols else "stock"

        insert_sql = f"INSERT OR IGNORE INTO products (name, price, {stock_col}, description) VALUES (?, ?, ?, ?)"
        data = [
            ("iPhone 11", 400, 10, 'Iphone 11 64 GB'),
            ("iPhone 12", 459, 67, 'Iphone 12 128 GB'),
            ("iPhone 13", 800, 10, 'Iphone 13 256 GB'),
            ("iPhone 14", 850, 150, 'Iphone 14 512 GB'),
            ("iPhone 15", 900, 150, 'Iphone 15 1 TB'),
            ("iPhone 16", 1200, 550, 'Iphone 16 2 TB'),
        ]
        conn.executemany(insert_sql, data)

if __name__ == "__main__":
    main()
