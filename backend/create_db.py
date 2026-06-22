import sqlite3
import csv

# Database se connect
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Employee table create
cursor.execute("""
CREATE TABLE IF NOT EXISTS employee (
    emp_id INTEGER PRIMARY KEY,
    employee_name TEXT,
    pf_number TEXT,
    department TEXT,
    designation TEXT,
    joining_date TEXT,
    mobile TEXT
)
""")

print("Employee table created successfully!")

# CSV data database me insert
with open("data/employee_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        cursor.execute("""
        INSERT OR IGNORE INTO employee
        (emp_id, employee_name, pf_number, department,
         designation, joining_date, mobile)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            row["emp_id"],
            row["employee_name"],
            row["pf_number"],
            row["department"],
            row["designation"],
            row["joining_date"],
            row["mobile"]
        ))

conn.commit()

print("Employee data inserted successfully!")

# Database band
conn.close()




