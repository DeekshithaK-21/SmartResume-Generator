def build_resume_prompt(data):
    experience_text = ""
    for exp in data["experiences"]:
        experience_text += f"""
• {exp['job_title']} at {exp['company']} ({exp['duration']})
  {exp['description']}
"""

    education_text = ""
    for edu in data["education"]:
        education_text += f"""
• {edu['degree']} – {edu['university']} ({edu['grad_year']})
"""

    achievements_text = data["achievements"]

    return f"""
You are an expert professional resume writer.

IMPORTANT RULES:
- Do NOT use placeholders
- Do NOT invent facts
- Improve wording and clarity only
- Use strong action verbs
- Keep the resume ATS-friendly and concise

===== PERSONAL DETAILS =====
Name: {data['name']}
Phone: {data['phone']}
Email: {data['email']}
Location: {data['location']}

===== TARGET ROLE =====
{data['role']}

===== SKILLS =====
{data['skills']}

===== EXPERIENCE =====
{experience_text}

===== EDUCATION =====
{education_text}

===== ACHIEVEMENTS =====
{achievements_text}

FORMAT THE RESUME WITH THESE SECTIONS IN ORDER:
1. Header
2. Professional Summary
3. Skills
4. Experience
5. Education
6. Achievements (at the end)

Use Markdown formatting.
"""


