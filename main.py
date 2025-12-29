from flask import Flask, render_template, request, jsonify
import os


from flask import Flask, render_template, request, jsonify, send_from_directory
import PyPDF2

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
    for skill in ["python", "java", "javascript", "html", "css", "flask"]:
        if skill in text:
            skills.append(skill)

    education = "B.Tech / BE" if "education" in text else "Not found"

    return jsonify({
        "name": "Karthik",
        "role": "Developer",
        "skills": skills,
        "education": education,
        "projects": ["Portfolio Website", "AI Resume Parser"]
    })

@app.route("/uploads/<path:filename>")
def download_file(filename):
    return send_from_directory("uploads", filename)

if __name__ == "__main__":
    app.run(debug=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
