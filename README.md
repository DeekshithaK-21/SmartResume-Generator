🧠 SmartResume Generator 📄

AI-Powered | ATS-Friendly | Streamlit App

SmartResume Generator is an AI-powered resume creation tool built using Streamlit and the Google Gemini (2026 GenAI SDK).
It helps users generate professional, ATS-friendly resumes by enhancing only the provided information — no fake skills, no invented experience.

✨ Why SmartResume Generator?

🚫 No hallucinated content

🎯 Optimized for Applicant Tracking Systems (ATS)

🧑‍💼 Ideal for students, freshers, and professionals

⚡ Fast, clean, and easy-to-use UI

🚀 Key Features

✅ AI-Enhanced Resume Writing (Google Gemini)

✅ Uses 2026 GenAI SDK → from google import genai

✅ Supports multiple work experiences

✅ Supports multiple education entries

✅ Dedicated Achievements section

✅ Structured & ATS-friendly output

✅ Simple, clean Streamlit UI

✅ Free-tier compatible model selection

✅ Handles AI overloads & failures gracefully

✅ Dynamic forms using Streamlit session state

🛠️ Tech Stack

| Technology            | Purpose                              |
| --------------------- | ------------------------------------ |
| **Python**            | Core programming language            |
| **Streamlit**         | Frontend user interface              |
| **Google Gemini API** | AI-based resume enhancement          |
| **GenAI SDK (2026)**  | Latest Gemini integration            |
| **python-dotenv**     | Secure environment variable handling |

## 📂 Project Structure

```text
SmartResume-Generator/
│
├── app.py                 # Streamlit UI
├── resume_generator.py    # Gemini integration (2026 SDK)
├── prompt_templates.py    # Prompt engineering logic
├── requirements.txt       # Project dependencies
├── .env.example           # Environment variable template
└── README.md              # Project documentation
```



🔐 Environment Setup

Create a .env file in the project root directory:

GEMINI_API_KEY=your_api_key_here

⚠️ Important:
Never commit the .env file to GitHub. It contains sensitive API keys.

▶️ How to Run the Project (Windows)
# Navigate to project directory
cd SmartResume-Generator

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py

📌 The app will automatically open in your default web browser.

📌 Use Cases

🎓 Students building their first resume

💼 Professionals updating resumes quickly

🧪 Mini-project for GenAI + Streamlit

📄 ATS-optimized resume generation demo

🔮 Future Enhancements

📄 Resume export as PDF / DOCX

🎨 Multiple resume templates

🧠 Skill-gap suggestions (non-intrusive)

🌐 Multi-language resume support

📊 Resume ATS score analyzer
