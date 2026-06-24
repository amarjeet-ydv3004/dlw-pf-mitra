from flask import Flask, request
from flask_cors import CORS
import sqlite3
import re
from chatbot_responses import responses
from api.routes import api

app = Flask(__name__)
CORS(app)

app.register_blueprint(api)

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


    # Greetings
    if question in [
        "hello", "hi", "hii", "hiiii", "hey", "namaste"]:
       return responses["hello"]
    
    # Time Greetings
    if "good morning" in question:
        return responses["good morning"]
    
    if "good afternoon" in question:
        return responses["good afternoon"]
    
    if "good evening" in question:
        return responses["good evening"]
    
    if "good night" in question:
        return responses["good night"]
    
    # Thanks
    if "thanks" in question or "thank you" in question:
        return responses["thanks"]
    
    # Appreciation
    if any(word in question for word in [
        "good", "better", "best", "excellent",
        "great", "awesome", "nice", "ok", "okay"
    ]):
        return responses["appreciation"]
    
    # Jai Hind
    if "jai hind" in question:
        return responses["jai hind"]
    
    # PF
    if "pf" in question:
        return responses["pf"]
    
    # BLW History (pehle)
    if "history of blw" in question:
        return responses["history of blw"]
    
    # BLW / DLW
    if "blw" in question or "dlw" in question:
        return responses["blw"]
    
    # TTC
    if "ttc" in question or "technical training centre" in question:
        return responses["ttc"]
    
    # IT Centre
    if "it centre" in question or "it center" in question:
        return responses["it centre"]
    
    # Locomotives
    if "wap7" in question:
        return responses["wap7"]
    
    if "wag9" in question:
        return responses["wag9"]
    
    # Project
    if "developer" in question:
        return responses["developer"]
    
    if "about project" in question:
        return responses["about project"]
    
    if "technology" in question:
        return responses["technology used"]
    
    # Exact Match Fallback
    if question in responses:
        return responses[question]



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