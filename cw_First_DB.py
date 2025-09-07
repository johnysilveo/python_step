import sqlite3
import random

def main():
    conn = sqlite3.connect("fru_vagies.db")
    conn.execute("PRAGMA foreign_keys = ON;")
    cur = conn.cursor()

    cur.executescript("""

    
    CREATE TABLE IF NOT EXISTS fruits_n_vagies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        type TEXT NOT NULL,
        color TEXT NOT NULL,
        calorie_count INTEGER NOT NULL CHECK (calorie_count > 0),
        description TEXT NOT NULL
    );
    """)

    rows = [
        # Fruits
        ("Apple",        "fruit",      "red/green", 52, "Crisp, sweet-tart table fruit."),
        ("Banana",       "fruit",      "yellow",    89, "Soft, sweet, energy-dense snack."),
        ("Orange",       "fruit",      "orange",    47, "Citrus fruit rich in vitamin C."),
        ("Strawberry",   "fruit",      "red",       33, "Juicy berries, fragrant and sweet."),
        ("Blueberry",    "fruit",      "blue",      57, "Small berries; popular in desserts."),
        ("Mango",        "fruit",      "orange",    60, "Tropical, aromatic, very sweet."),
        ("Pineapple",    "fruit",      "brown/yel", 50, "Tropical fruit with tangy-sweet flesh."),
        ("Grape",        "fruit",      "green/purp",69, "Small juicy berries used for juice/wine."),
        ("Watermelon",   "fruit",      "green/red", 30, "Very hydrating melon, mild sweetness."),
        ("Kiwi",         "fruit",      "brown/green",61,"Tangy-sweet, bright green flesh."),
        ("Peach",        "fruit",      "orange",    39, "Soft stone fruit with floral aroma."),
        ("Pear",         "fruit",      "green",     57, "Sweet, grainy texture, juicy."),
        # Vegetables
        ("Carrot",       "vegetable",  "orange",    41, "Crunchy root, slightly sweet."),
        ("Broccoli",     "vegetable",  "green",     34, "Cruciferous florets, earthy flavor."),
        ("Spinach",      "vegetable",  "green",     23, "Leafy green, mild and tender."),
        ("Tomato",       "vegetable",  "red",       18, "Juicy, versatile in salads/sauces."),
        ("Cucumber",     "vegetable",  "green",     15, "Very hydrating, crisp texture."),
        ("Bell pepper",  "vegetable",  "red",       31, "Sweet pepper, thick crunchy walls."),
        ("Onion",        "vegetable",  "white",     40, "Pungent bulb, sweetens when cooked."),
        ("Potato",       "vegetable",  "brown",     77, "Starchy tuber, many cooking uses."),
        ("Sweet potato", "vegetable",  "orange",    86, "Sweet, beta-carotene rich tuber."),
        ("Lettuce",      "vegetable",  "green",     15, "Leafy, crisp, mild flavor."),
        ("Zucchini",     "vegetable",  "green",     17, "Tender summer squash."),
        ("Eggplant",     "vegetable",  "purple",    25, "Spongy flesh, absorbs flavors well."),
    ]


    # before = conn.total_changes
    # cur.executemany(
    #     'INSERT OR IGNORE INTO fruits_n_vagies (name, "type", color, calorie_count, description) '
    #     'VALUES (?, ?, ?, ?, ?)',
    #     rows
    # )
    # inserted = conn.total_changes - before

    # cur.execute("SELECT COUNT(*) FROM fruits_n_vagies")
    # total = cur.fetchone()[0]
    # print(f"Inserted: {inserted} new rows. Total rows now: {total}")

    print("\n\t\tFruits in alphabetical order:")
    cur.execute('SELECT * FROM fruits_n_vagies WHERE "type" = ? ORDER BY name COLLATE NOCASE ASC;', ("fruit",))
    for fruit in cur.fetchall():
        print(fruit)

    print("\n\t\tVegetables sorted by color, then calories:")
    cur.execute(
        'SELECT * FROM fruits_n_vagies '
        'WHERE "type" = ? '
        'ORDER BY color COLLATE NOCASE ASC, calorie_count ASC, name COLLATE NOCASE ASC;',
        ("vegetable",)
    )
    print("\n\t\t Vgetables sorted by ")
    for veg in cur.fetchall():
        print(veg)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()