import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def get_ai_suggestions(resume_text, job_description):

    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY")
    )

    prompt = f"""
You are an AI Resume Analyzer.

Analyze the following resume against the job description.

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}

Give a concise analysis with these sections:

1. Resume Strengths
2. Missing or Weak Areas
3. Keyword Suggestions
4. Project Suggestions
5. Overall Advice

Important:
- Do not invent experience for the candidate.
- Only suggest a skill if the candidate genuinely has that skill.
- Keep the advice practical for a student or fresher.
"""

    response = client.responses.create(
        model="gpt-5.6-luna",
        input=prompt
    )

    return response.output_text
