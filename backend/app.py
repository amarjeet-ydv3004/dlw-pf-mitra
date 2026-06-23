from flask import Flask, request
from flask_cors import CORS
import sqlite3
import re

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "PF Mitra API Running"


@app.route("/ask")
def ask():

    name = request.args.get("name")

    if not name:
        return "Please enter a query"

    # Input Cleaning
    question = re.sub(r'[^a-zA-Z0-9 ]', '', name)
    question = question.lower().strip()

    # =========================
    # KNOWLEDGE BASE
    # =========================

    if question in ["hello", "hi", "hii", "hiiii", "namaste"]:
        return """
<div class='result-card'>
<h3>👋 Welcome</h3>
<p>Hello! Welcome to PF Mitra Chatbot.</p>
</div>
"""

    if question == "good morning":
        return """
<div class='result-card'>
<h3>🌞 Good Morning</h3>
<p>Welcome to PF Mitra Chatbot.</p>
</div>
"""

    if question == "good evening":
        return """
<div class='result-card'>
<h3>🌆 Good Evening</h3>
<p>Welcome to PF Mitra Chatbot.</p>
</div>
"""

    if question == "good night":
        return """
<div class='result-card'>
<h3>🌙 Good Night</h3>
<p>Thank you for using PF Mitra Chatbot.</p>
</div>
"""

    if question in ["thanks", "thank you"]:
        return """
<div class='result-card'>
<h3>🙏 Thank You</h3>
<p>You are welcome!</p>
</div>
"""

    if question == "blw":
        return """
<div class='result-card'>
<h3>🏭 About BLW</h3>
<p>
Banaras Locomotive Works (BLW), formerly Diesel Locomotive Works (DLW),
is a major locomotive manufacturing unit of Indian Railways located in Varanasi.
</p>
</div>
"""

    if question == "ttc":
        return """
<div class='result-card'>
<h3>🎓 Technical Training Centre (TTC)</h3>
<p>
TTC provides training for railway staff,
apprentices and engineering students.
</p>
</div>
"""

    if question in ["it centre", "it center"]:
        return """
<div class='result-card'>
<h3>💻 IT Centre</h3>
<p>
IT Centre manages website, applications,
database and IT services of BLW.
</p>
</div>
"""

    if question == "wap7":
        return """
<div class='result-card'>
<h3>🚆 WAP-7</h3>
<p>
WAP-7 is a high-speed electric passenger locomotive
used by Indian Railways.
</p>
</div>
"""

    if question == "wag9":
        return """
<div class='result-card'>
<h3>🚆 WAG-9</h3>
<p>
WAG-9 is a powerful electric freight locomotive
used for hauling heavy goods trains.
</p>
</div>
"""

    # =========================
    # DATABASE SEARCH
    # =========================

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
    """
    SELECT employee_name, pf_number, department, designation
    FROM employee
    WHERE LOWER(REPLACE(employee_name,' ',''))
          = LOWER(REPLACE(?,' ',''))
       OR LOWER(pf_number) = LOWER(?)
    """,
    (name, name)
    )

    result = cursor.fetchone()

    conn.close()

    if result:
        return f"""
<div class='result-card'>

<h3>Employee Details</h3>

<p><b>Employee Name:</b> {result[0]}</p>

<p><b>PF Number:</b> {result[1]}</p>

<p><b>Department:</b> {result[2]}</p>

<p><b>Designation:</b> {result[3]}</p>

</div>
"""
    else:
        return """
<div class='result-card'>
<h3>❌ Not Found</h3>
<p>Information not available.</p>
</div>
"""


if __name__ == "__main__":
    app.run(debug=True)