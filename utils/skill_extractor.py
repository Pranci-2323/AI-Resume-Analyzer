import re


SKILLS = [
    "java",
    "python",
    "c++",
    "c",
    "javascript",
    "typescript",
    "html",
    "css",
    "react",
    "react.js",
    "node.js",
    "express.js",
    "spring boot",
    "sql",
    "mysql",
    "mongodb",
    "git",
    "github",
    "docker",
    "aws",
    "machine learning",
    "deep learning",
    "tensorflow",
    "pytorch",
    "nlp",
    "flask",
    "fastapi",
    "pandas",
    "numpy",
    "scikit-learn",
    "tailwind css",
    "rest api",
    "data structures",
    "algorithms"
]


def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in SKILLS:

        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text):
            found_skills.append(skill)

    return found_skills