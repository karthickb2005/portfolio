from flask import Flask, request, jsonify, render_template
import PyPDF2
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/", methods=["GET", "POST"])
def index():
    skills = []
    if request.method == "POST":
        file = request.files["resume"]

        if file:
            reader = PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()

            skills = extract_skills_from_text(text)

    return render_template("index.html", skills=skills)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
from flask import Flask, render_template, request
from PyPDF2 import PdfReader
import re

app = Flask(__name__)

def extract_skills_from_text(text):
    skills_list = [
        "python", "java", "c++", "html", "css", "javascript",
        "flask", "django", "react", "sql", "machine learning",
        "data science", "ai", "deep learning"
    ]
    found = []
    text = text.lower()

    for skill in skills_list:
        if skill in text:
            found.append(skill.capitalize())

    return list(set(found))
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
