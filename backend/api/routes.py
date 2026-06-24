from flask import Blueprint

api = Blueprint("api", __name__)

@api.route("/status")
def status():
    return {
        "project": "PF Mitra Chatbot",
        "developer": "Amarjeet Yadav",
        "status": "Running"
    }