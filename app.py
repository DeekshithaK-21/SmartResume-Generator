import streamlit as st
from prompt_templates import build_resume_prompt
from resume_generator import generate_resume

st.set_page_config(page_title="SmartResume Generator", layout="centered")

st.title("📄 SmartResume Generator")
st.caption("AI-powered, ATS-friendly resume builder")

# ---------- CLEAR ----------
if st.button("🗑️ Clear All Resume Data"):
    st.session_state.clear()
    st.rerun()


# ---------- PERSONAL DETAILS ----------
st.header("Personal Details")
name = st.text_input("Full Name")
phone = st.text_input("Phone Number")
email = st.text_input("Email Address")
location = st.text_input("City, State")

role = st.selectbox(
    "Target Job Role",
    [
        "Software Engineer",
        "Data Analyst",
        "Marketing Specialist",
        "Graphic Designer",
        "Freelancer"
    ]
)

skills = st.text_area(
    "Skills (comma-separated)",
    placeholder="Python, SQL, Data Analysis, GenAI"
)

# ---------- SESSION STATE ----------
st.session_state.setdefault("experiences", [])
st.session_state.setdefault("education", [])

# ---------- WORK EXPERIENCE ----------
st.header("Work Experience")

with st.form("experience_form", clear_on_submit=True):
    company = st.text_input("Company Name")
    job_title = st.text_input("Job Title")
    duration = st.text_input("Duration (e.g., Jan 2023 – Jan 2025)")
    description = st.text_area("Responsibilities")
    add_exp = st.form_submit_button("➕ Add Experience")

    if add_exp:
        if not all([company, job_title, duration, description]):
            st.warning("Please fill all experience fields.")
        else:
            st.session_state.experiences.append({
                "company": company,
                "job_title": job_title,
                "duration": duration,
                "description": description
            })

for i, exp in enumerate(st.session_state.experiences, 1):
    st.markdown(f"**{i}. {exp['job_title']} – {exp['company']} ({exp['duration']})**")

# ---------- EDUCATION ----------
st.header("Education")

with st.form("education_form", clear_on_submit=True):
    degree = st.text_input("Degree")
    university = st.text_input("University")
    grad_year = st.text_input("Graduation Year")
    add_edu = st.form_submit_button("➕ Add Education")

    if add_edu:
        if not all([degree, university, grad_year]):
            st.warning("Please fill all education fields.")
        else:
            st.session_state.education.append({
                "degree": degree,
                "university": university,
                "grad_year": grad_year
            })

for i, edu in enumerate(st.session_state.education, 1):
    st.markdown(f"**{i}. {edu['degree']} – {edu['university']} ({edu['grad_year']})**")

# ---------- ACHIEVEMENTS ----------
st.header("Achievements (Overall)")

achievements = st.text_area(
    "Achievements / Awards / Certifications",
    placeholder=(
        "• Secured 1st place in college hackathon\n"
        "• Completed Google Data Analytics Certification\n"
        "• Reduced report generation time by 30%"
    )
)

# ---------- GENERATE ----------
if st.button("✨ Generate Resume"):
    if not all([name, phone, email, location, skills]) \
       or not st.session_state.experiences \
       or not st.session_state.education \
       or not achievements:
        st.warning("Please complete all sections before generating.")
    else:
        data = {
            "name": name,
            "phone": phone,
            "email": email,
            "location": location,
            "role": role,
            "skills": skills,
            "experiences": st.session_state.experiences,
            "education": st.session_state.education,
            "achievements": achievements
        }

        with st.spinner("Crafting your resume..."):
            prompt = build_resume_prompt(data)
            resume_text = generate_resume(prompt)

        st.subheader("Generated Resume")
        st.markdown(resume_text)
