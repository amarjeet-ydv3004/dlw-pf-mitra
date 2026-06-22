from flask import Flask, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "PF Mitra API Running"

@app.route("/ask")
def ask():

    name = request.args.get("name")

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
    """
    SELECT pf_number, department, designation
    FROM employee
    WHERE LOWER(REPLACE(employee_name,' ',''))
          = LOWER(REPLACE(?,' ',''))
    """,
    (name,)
)
    result = cursor.fetchone()

    conn.close()

    if result:
        return f"""
PF Number: {result[0]}
Department: {result[1]}
Designation: {result[2]}
"""
    else:
        return "Employee not found"

if __name__ == "__main__":
    app.run(debug=True)



    