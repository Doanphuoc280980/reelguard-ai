# ReelGuard AI - Mindful Scrolling Assistant

> Developed for the **Meta Global AI Developer Hackathon 2026** (Track: *Build for Your World*).

## 💡 Project Overview
Scrolling through Facebook Reels is one of the biggest drivers of mindless time-wasting (doomscrolling) and attention fatigue. **ReelGuard AI** is a smart assistant powered by the **Meta Model API** that analyzes content consumption behavior and delivers personalized, empathetic nudges to help users mindfully pause and reconnect with their real-world goals.

---

## 🛠️ Tech Stack
- **AI Core:** Meta Model API (`muse-spark`)
- **Backend:** Python, FastAPI, Pydantic
- **Infrastructure:** Docker, Uvicorn

---

## 📂 Project Structure
- `main.py`: FastAPI application entry point and endpoints.
- `services.py`: Integration logic with Meta Model API for generating empathetic nudges.
- `models.py`: Pydantic data models for session analysis.
- `config.py`: Environment configurations and alert thresholds.
- `requirements.txt`: Project Python dependencies.
- `Dockerfile`: Containerization configuration.

---

## 🚀 Getting Started Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Doanphuoc280980/reelguard-ai.git](https://github.com/Doanphuoc280980/reelguard-ai.git)
   cd reelguard-ai
Install dependencies:

Bash
pip install -r requirements.txt
Run the application:

Bash
uvicorn main:app --reload
