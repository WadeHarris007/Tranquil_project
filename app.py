from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
import os

app = Flask(__name__)

# Replace with your own MongoDB URI
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(MONGO_URI)
db = client["tranquil_times"]
feedback_collection = db["feedback"]

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/submit-feedback", methods=["POST"])
def submit_feedback():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    feedback_data = {
        "name": name,
        "email": email,
        "message": message
    }

    feedback_collection.insert_one(feedback_data)

    return redirect("/thank-you")

@app.route("/thank-you")
def thank_you():
    return "<h2>Thank you for your feedback!</h2><p><a href='/contact'>Back to Contact Page</a></p>"

if __name__ == "__main__":
    app.run(debug=True)
