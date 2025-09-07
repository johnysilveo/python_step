import sqlite3



def main():
    conn = sqlite3.connect("Sales.db")
    conn.execute("PRAGMA foreign_keys = ON;")
    cur = conn.cursor()

    # 1) Schema: Salesmen, Customers, Sales
    cur.executescript("""
    CREATE TABLE IF NOT EXISTS Salesmen(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        hire_date TEXT
    );

    CREATE TABLE IF NOT EXISTS Customers(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        city TEXT
    );

    CREATE TABLE IF NOT EXISTS Sales(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        salesman_id INTEGER NOT NULL,
        customer_id INTEGER NOT NULL,
        amount NUMERIC NOT NULL CHECK (amount > 0),
        sale_date TEXT NOT NULL,           -- ISO date YYYY-MM-DD
        FOREIGN KEY (salesman_id) REFERENCES Salesmen(id)
            ON UPDATE CASCADE ON DELETE RESTRICT,
        FOREIGN KEY (customer_id) REFERENCES Customers(id)
            ON UPDATE CASCADE ON DELETE RESTRICT
    );

    CREATE INDEX IF NOT EXISTS idx_sales_salesman ON Sales(salesman_id);
    CREATE INDEX IF NOT EXISTS idx_sales_customer ON Sales(customer_id);
    CREATE INDEX IF NOT EXISTS idx_sales_amount   ON Sales(amount);
    """)

    # 2) Seed tiny dataset once
    cur.execute("SELECT COUNT(*) FROM Sales;")
    if cur.fetchone()[0] == 0:
        salesmen = [
            ("Alice Reed", "2020-02-10"),
            ("Bob Lin",    "2019-06-01"),
            ("Carla Diaz", "2021-09-15"),
        ]
        customers = [
            ("Acme Corp",   "Kyiv"),
            ("Globex LLC",  "Lviv"),
            ("Initech",     "Odesa"),
            ("Umbrella SA", "Kharkiv"),
        ]
        cur.executemany("INSERT OR IGNORE INTO Salesmen(name, hire_date) VALUES(?, ?);", salesmen)
        cur.executemany("INSERT OR IGNORE INTO Customers(name, city) VALUES(?, ?);", customers)

        # (salesman_name, customer_name, amount, date)
        sample_sales = [
            ("Alice Reed", "Acme Corp",   1200.00, "2025-08-01"),
            ("Alice Reed", "Globex LLC",  5000.00, "2025-08-05"),
            ("Alice Reed", "Initech",       850.00, "2025-08-12"),
            ("Bob Lin",    "Acme Corp",    2300.00, "2025-08-03"),
            ("Bob Lin",    "Initech",      1500.00, "2025-08-10"),
            ("Bob Lin",    "Umbrella SA",  3000.00, "2025-08-18"),
            ("Carla Diaz", "Acme Corp",    7500.00, "2025-08-06"),
            ("Carla Diaz", "Globex LLC",    250.00, "2025-08-14"),
            ("Carla Diaz", "Umbrella SA",  4200.00, "2025-08-20"),
            ("Carla Diaz", "Initech",       900.00, "2025-08-22"),
        ]

        # resolve names to IDs and insert
        for sm_name, cu_name, amount, d in sample_sales:
            sm_id = cur.execute("SELECT id FROM Salesmen WHERE name = ?;", (sm_name,)).fetchone()[0]
            cu_id = cur.execute("SELECT id FROM Customers WHERE name = ?;", (cu_name,)).fetchone()[0]
            cur.execute(
                "INSERT INTO Sales(salesman_id, customer_id, amount, sale_date) VALUES(?,?,?,?);",
                (sm_id, cu_id, amount, d)
            )

    # 3) The 13 queries (as SQL strings)
    Q_ALL_DEALS = """
        SELECT s.id AS sale_id, sm.name AS salesman, c.name AS customer, s.amount, s.sale_date
        FROM Sales s
        JOIN Salesmen sm ON sm.id = s.salesman_id
        JOIN Customers c ON c.id = s.customer_id
        ORDER BY s.id;
    """
    Q_DEALS_BY_SALESMAN = """
        SELECT s.id AS sale_id, sm.name AS salesman, c.name AS customer, s.amount, s.sale_date
        FROM Sales s
        JOIN Salesmen sm ON sm.id = s.salesman_id
        JOIN Customers c ON c.id = s.customer_id
        WHERE sm.name = ?
        ORDER BY s.amount DESC;
    """
    Q_MAX_DEAL_OVERALL = """
        SELECT s.id AS sale_id, sm.name AS salesman, c.name AS customer, s.amount, s.sale_date
        FROM Sales s
        JOIN Salesmen sm ON sm.id = s.salesman_id
        JOIN Customers c ON c.id = s.customer_id
        ORDER BY s.amount DESC, s.id ASC LIMIT 1;
    """
    Q_MIN_DEAL_OVERALL = """
        SELECT s.id AS sale_id, sm.name AS salesman, c.name AS customer, s.amount, s.sale_date
        FROM Sales s
        JOIN Salesmen sm ON sm.id = s.salesman_id
        JOIN Customers c ON c.id = s.customer_id
        ORDER BY s.amount ASC, s.id ASC LIMIT 1;
    """
    Q_MAX_BY_SALESMAN = """
        SELECT s.id AS sale_id, sm.name AS salesman, c.name AS customer, s.amount, s.sale_date
        FROM Sales s
        JOIN Salesmen sm ON sm.id = s.salesman_id
        JOIN Customers c ON c.id = s.customer_id
        WHERE sm.name = ?
        ORDER BY s.amount DESC, s.id ASC LIMIT 1;
    """
    Q_MIN_BY_SALESMAN = """
        SELECT s.id AS sale_id, sm.name AS salesman, c.name AS customer, s.amount, s.sale_date
        FROM Sales s
        JOIN Salesmen sm ON sm.id = s.salesman_id
        JOIN Customers c ON c.id = s.customer_id
        WHERE sm.name = ?
        ORDER BY s.amount ASC, s.id ASC LIMIT 1;
    """
    Q_MAX_BY_CUSTOMER = """
        SELECT s.id AS sale_id, sm.name AS salesman, c.name AS customer, s.amount, s.sale_date
        FROM Sales s
        JOIN Salesmen sm ON sm.id = s.salesman_id
        JOIN Customers c ON c.id = s.customer_id
        WHERE c.name = ?
        ORDER BY s.amount DESC, s.id ASC LIMIT 1;
    """
    Q_MIN_BY_CUSTOMER = """
        SELECT s.id AS sale_id, sm.name AS salesman, c.name AS customer, s.amount, s.sale_date
        FROM Sales s
        JOIN Salesmen sm ON sm.id = s.salesman_id
        JOIN Customers c ON c.id = s.customer_id
        WHERE c.name = ?
        ORDER BY s.amount ASC, s.id ASC LIMIT 1;
    """
    Q_TOP_SALESMAN_TOTAL = """
        SELECT sm.name AS salesman, SUM(s.amount) AS total_sales, COUNT(*) AS deals
        FROM Sales s
        JOIN Salesmen sm ON sm.id = s.salesman_id
        GROUP BY sm.id
        ORDER BY total_sales DESC, sm.name ASC
        LIMIT 1;
    """
    Q_BOTTOM_SALESMAN_TOTAL = """
        SELECT sm.name AS salesman, SUM(s.amount) AS total_sales, COUNT(*) AS deals
        FROM Sales s
        JOIN Salesmen sm ON sm.id = s.salesman_id
        GROUP BY sm.id
        ORDER BY total_sales ASC, sm.name ASC
        LIMIT 1;
    """
    Q_TOP_CUSTOMER_TOTAL = """
        SELECT c.name AS customer, SUM(s.amount) AS total_purchases, COUNT(*) AS deals
        FROM Sales s
        JOIN Customers c ON c.id = s.customer_id
        GROUP BY c.id
        ORDER BY total_purchases DESC, c.name ASC
        LIMIT 1;
    """
    Q_AVG_BY_CUSTOMER = """
        SELECT c.name AS customer, AVG(s.amount) AS avg_purchase, COUNT(*) AS deals
        FROM Sales s
        JOIN Customers c ON c.id = s.customer_id
        WHERE c.name = ?
        GROUP BY c.id;
    """
    Q_AVG_BY_SALESMAN = """
        SELECT sm.name AS salesman, AVG(s.amount) AS avg_sale, COUNT(*) AS deals
        FROM Sales s
        JOIN Salesmen sm ON sm.id = s.salesman_id
        WHERE sm.name = ?
        GROUP BY sm.id;
    """

    # 4) Demo runs (you can remove these prints if you only need the SQL)
    print("1) All deals:")
    for row in cur.execute(Q_ALL_DEALS):
        print(row)

    print("\n2) Deals of a specific salesman (Alice Reed):")
    for row in cur.execute(Q_DEALS_BY_SALESMAN, ("Alice Reed",)):
        print(row)

    print("\n3) Max amount deal (overall):")
    print(cur.execute(Q_MAX_DEAL_OVERALL).fetchone())

    print("\n4) Min amount deal (overall):")
    print(cur.execute(Q_MIN_DEAL_OVERALL).fetchone())

    print("\n5) Max deal for a specific salesman (Bob Lin):")
    print(cur.execute(Q_MAX_BY_SALESMAN, ("Bob Lin",)).fetchone())

    print("\n6) Min deal for a specific salesman (Bob Lin):")
    print(cur.execute(Q_MIN_BY_SALESMAN, ("Bob Lin",)).fetchone())

    print("\n7) Max deal for a specific customer (Acme Corp):")
    print(cur.execute(Q_MAX_BY_CUSTOMER, ("Acme Corp",)).fetchone())

    print("\n8) Min deal for a specific customer (Acme Corp):")
    print(cur.execute(Q_MIN_BY_CUSTOMER, ("Acme Corp",)).fetchone())

    print("\n9) Salesman with maximum total sales:")
    print(cur.execute(Q_TOP_SALESMAN_TOTAL).fetchone())

    print("\n10) Salesman with minimum total sales:")
    print(cur.execute(Q_BOTTOM_SALESMAN_TOTAL).fetchone())

    print("\n11) Customer with maximum total purchases:")
    print(cur.execute(Q_TOP_CUSTOMER_TOTAL).fetchone())

    print("\n12) Average purchase for a specific customer (Globex LLC):")
    print(cur.execute(Q_AVG_BY_CUSTOMER, ("Globex LLC",)).fetchone())

    print("\n13) Average purchase for a specific salesman (Carla Diaz):")
    print(cur.execute(Q_AVG_BY_SALESMAN, ("Carla Diaz",)).fetchone())

    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()
