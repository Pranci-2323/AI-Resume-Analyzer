from flask import Flask, render_template, request
from utils.resume_parser import extract_resume_text
from utils.skill_extractor import extract_skills
from utils.matcher import match_skills
from utils.ai_analyzer import get_ai_suggestions

from dotenv import load_dotenv

import os


load_dotenv()


app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Analyze Resume
@app.route("/analyze", methods=["POST"])
def analyze():

    # Get uploaded resume
    resume = request.files.get("resume")

    if not resume:
        return "Please upload a resume."

    if resume.filename == "":
        return "Please select a resume."


    # Save resume
    file_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        resume.filename
    )

    resume.save(file_path)


    # Extract text from resume
    resume_text = extract_resume_text(file_path)


    # Extract skills from resume
    skills = extract_skills(resume_text)


    # Get job description
    job_description = request.form.get(
        "job_description",
        ""
    )


    # Extract skills from job description
    job_skills = extract_skills(job_description)


    # Compare resume skills with job skills
    matched_skills, missing_skills, match_percentage = match_skills(
        skills,
        job_skills
    )

    ai_suggestions = get_ai_suggestions(

        resume_text,
        job_description
    )


    # Send results to HTML
    return render_template(
    "index.html",
    resume_text=resume_text,
    skills=skills,
    job_skills=job_skills,
    matched_skills=matched_skills,
    missing_skills=missing_skills,
    match_percentage=match_percentage,
    ai_suggestions=ai_suggestions
)


# Start Flask
if __name__ == "__main__":
    app.run(debug=True)