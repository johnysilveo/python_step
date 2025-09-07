import sqlite3


def main():
    conn = sqlite3.connect("students_marks.db")
    conn.execute("PRAGMA foreign_keys = ON;")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name TEXT NOT NULL,
    city TEXT NOT NULL,
    country TEXT NOT NULL,
    dob INTEGER NOT NULL,
    email TEXT NOT NULL,
    phone_number TEXT NOT NULL,
    group_name TEXT NOT NULL,
    avg_mark_all NUMERIC NOT NULL,
    avg_subject_mark NUMERIC NOT NULL);""")

    # students_seed = [
    #     ("Alice Johnson",     "New York",      "USA", 20040214, "alice.johnson@example.com",     "5551230011", "CS-101", 87.5, 85.2),
    #     ("Brian Smith",       "Los Angeles",   "USA", 20031003, "brian.smith@example.com",       "5551230012", "CS-101", 91.3, 92.0),
    #     ("Chloe Martinez",    "Chicago",       "USA", 20050322, "chloe.martinez@example.com",    "5551230013", "CS-102", 78.9, 80.5),
    #     ("Daniel Thompson",   "Houston",       "USA", 20040611, "daniel.thompson@example.com",   "5551230014", "CS-102", 84.2, 83.0),
    #     ("Emma Williams",     "Seattle",       "USA", 20021230, "emma.williams@example.com",     "5551230015", "CS-201", 95.1, 94.4),
    #     ("Franklin Lee",      "Boston",        "USA", 20050807, "franklin.lee@example.com",      "5551230016", "CS-201", 72.6, 70.8),
    #     ("Grace Kim",         "San Francisco", "USA", 20031119, "grace.kim@example.com",         "5551230017", "CS-202", 88.0, 89.1),
    #     ("Henry Brown",       "Austin",        "USA", 20040305, "henry.brown@example.com",       "5551230018", "CS-202", 82.4, 81.7),
    # ]

    # cur.execute("SELECT COUNT(*) FROM students;")
    # if cur.fetchone()[0] == 0:
    #     cur.executemany("""
    #         INSERT INTO students
    #             (name, city, country, dob, email, phone_number, group_name, avg_mark_all, avg_subject_mark)
    #         VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
    #     """, students_seed)

    

    for row in cur.execute("SELECT * FROM students ORDER BY id;"):
        print(row)

    for row in cur.execute("select id, name from students "
                           "GROUP BY id;"):
        print(row)

    for row in cur.execute("select avg_mark_all, name, id  "
                           "from students "
                           "order by avg_mark_all desc;"):
        print(row)

    for row in cur.execute("select * "
                           "from students "
                           "where avg_mark_all >= 85 "
                           "order by avg_mark_all desc;"):
        print(row)

    for row in cur.execute("select distinct country "
                           " from students; "):
        print(row)

    for row in cur.execute("select distinct city  "
                           " from students; "):
        print(row)

    for row in cur.execute("select distinct group_name,name "
                           "from students;"):
        print(row)

    for row in cur.execute("select name, avg_subject_mark "
                           "from students "
                           ";"):
        print(row)

    #>>>>>>>>>>>>>>>>>> SECOND <<<<<<<<<<<<<<<<<<<

    for row in cur.execute("select name, avg_mark_all "
                           "from students "
                           "where avg_mark_all between 70 and 84;"):
        print(row)

    for row in cur.execute("select * from students "
                           "where dob >= 20050903;"):
        print(row)

    for row in cur.execute("select * "
                           "from students "
                           "where dob between 20000000 and 20060000;"):
        print(row)

    for row in cur.execute("select * "
                           "from students "
                           "where name like 'franklin%';"):
        print(row)

    for row in cur.execute("select phone_number, name, id  "
                           "from students "
                           "where phone_number like '555%';"):
        print(row)

    for row in cur.execute("select email, name, id "
                           "from students "
                           "where email like 'f%';"):
        print(row)

    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()

# def main():
#     conn = sqlite3.connect("Hospital.db")
#     conn.execute("PRAGMA foreign_keys = ON;")
#     cur = conn.cursor()
#
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS Departments(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         Building INTEGER NOT NULL CHECK (Building BETWEEN 1 AND 5),
#         Financing NUMERIC NOT NULL DEFAULT 0 CHECK(Financing >= 0),
#         Name TEXT NOT NULL UNIQUE CHECK (length(trim(Name)) > 0)
#     );
#
#     CREATE TABLE IF NOT EXISTS Diseases(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         Name NVARCHAR(100) NOT NULL UNIQUE CHECK (length(trim(Name)) > 0),
#         Severity INTEGER NOT NULL DEFAULT 1 CHECK (Severity >= 1)
#     );
#
#     CREATE TABLE IF NOT EXISTS Doctors(
#         id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#         Name NVARCHAR(max) NOT NULL CHECK (length(trim(Name)) > 0),
#         Phone CHAR(10),
#         Salary NUMERIC NOT NULL CHECK (Salary > 0),
#         Surname NVARCHAR(MAX) NOT NULL CHECK (length(trim(Surname)) > 0)
#     );
#
#     CREATE TABLE IF NOT EXISTS Examinations(
#         id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#         day_of_week INTEGER NOT NULL CHECK (day_of_week BETWEEN 1 AND 7),
#         start_time TEXT NOT NULL CHECK (start_time BETWEEN '08:00' AND '18:00'),
#         end_time TEXT NOT NULL CHECK (end_time > start_time),
#         name NVARCHAR(100) NOT NULL UNIQUE CHECK (length(trim(name)) > 0)
#     );
#
#     CREATE TABLE IF NOT EXISTS Wards(
#     id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#     building INTEGER NOT NULL CHECK (building BETWEEN 1 AND 5),
#     floor INTEGER NOT NULL CHECK (floor >= 1),
#     name NVARCHAR(20) NOT NULL UNIQUE CHECK (length(trim(name)) > 0)
#     );
#
#     """)
#
#     conn.commit()
#     conn.close()
#
# if __name__ == '__main__':
#     main()