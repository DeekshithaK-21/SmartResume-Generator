# SmartResume Generator 🧠📄

An AI-powered resume generator built using **Streamlit** and **Google Gemini (2026 GenAI SDK)**.  
The application helps users create **ATS-friendly, professional resumes** by combining structured user input with AI-enhanced wording — without inventing facts.

---

## 🚀 Features

- ✅ AI-enhanced resume generation (Google Gemini)
- ✅ 2026-ready GenAI SDK (`from google import genai`)
- ✅ Multiple work experiences & education entries
- ✅ Separate **Achievements** section
- ✅ ATS-friendly structured output
- ✅ Clean and simple UI (Streamlit)
- ✅ Free-tier compatible model selection
- ✅ Graceful handling of AI overloads
- ✅ Session-state based dynamic forms

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **Google Gemini API (GenAI SDK – 2026)**
- **python-dotenv**

---

## 📂 Project Structure

SmartResume-Generator/
│
├── app.py # Streamlit UI
├── resume_generator.py # Gemini integration (2026 SDK)
├── prompt_templates.py # Prompt engineering logic
├── requirements.txt # Dependencies
├── .env.example # Environment variable template
└── README.md

## 🔐 Environment Setup

Create a `.env` file in the project root:

GEMINI_API_KEY=your_api_key_here
⚠️ Do NOT commit .env to GitHub

▶️ How to Run the Project (Windows)
bash
# Navigate to project
cd SmartResume-Generator

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
The app will open automatically in your browser.