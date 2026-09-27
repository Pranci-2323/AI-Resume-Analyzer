
# 🤖 AI Resume Analyzer

An AI-powered web application that analyzes resumes and compares them with job descriptions to provide useful insights such as **ATS score, skill matching, missing skills, and AI-generated resume feedback**.

## 🚀 Features

- 📄 Upload resumes in PDF format
- 🔍 Extract text from resumes automatically
- 🧠 Extract relevant skills from resumes
- 📋 Compare resume skills with a job description
- 📊 Generate an ATS-style compatibility score
- 🎯 Identify matching and missing skills
- 🤖 Generate AI-powered resume analysis
- 💻 Simple and user-friendly web interface

## 🛠️ Tech Stack

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- Flask

### AI & Machine Learning
- OpenAI API
- NLP-based text processing

### Libraries & Tools
- PyPDF2
- Python-dotenv
- Joblib
- Scikit-learn

## 📂 Project Structure

```text
AI-Resume-Analyzer/
│
├── static/
│   ├── script.js
│   └── style.css
│
├── templates/
│   └── index.html
│
├── utils/
│   ├── __init__.py
│   ├── ai_analyzer.py
│   ├── matcher.py
│   ├── resume_parser.py
│   └── skill_extractor.py
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
