def match_skills(resume_skills, job_skills):

    resume_skills = set(resume_skills)
    job_skills = set(job_skills)

    matched_skills = resume_skills.intersection(job_skills)

    missing_skills = job_skills - resume_skills

    if len(job_skills) > 0:
        match_percentage = (
            len(matched_skills) / len(job_skills)
        ) * 100
    else:
        match_percentage = 0

    return (
        list(matched_skills),
        list(missing_skills),
        round(match_percentage, 2)
    )