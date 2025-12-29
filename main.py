from flask import Flask, request, jsonify, render_template
import PyPDF2
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["resume"]
    reader = PyPDF2.PdfReader(file)

    text = ""
    for page in reader.pages:
        text += page.extract_text().lower()

    skills = []
    for s in ["python", "java", "javascript", "html", "css", "flask"]:
        if s in text:
            skills.append(s)

    return {
        "name": "Karthik",
        "role": "Developer",
        "skills": skills
    }

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
