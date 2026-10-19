# 🚀 AI SaaS Product – Local LLM-Powered Analytics Platform

## 📌 Project Description

This project is a **production-style AI SaaS application** that provides **data analysis and intelligent responses using a locally hosted Large Language Model (LLM)**. It is designed to simulate how modern SaaS platforms process logs, apply business rules, and use AI models to deliver structured insights through an API and UI.

The goal of this project is to **demonstrate real-world backend + AI + API design skills** that are highly relevant for **Software Engineer / AI Engineer / Backend roles**.

Key highlights:

* End-to-end system (Frontend → Backend → AI Model)
* Uses **local LLM (Ollama / LLaMA3)** – no paid APIs
* Clean architecture with scalable components
* Interview-ready, real SaaS-style implementation

---

## 🧠 System Architecture

```
User (React UI)
     |
FastAPI API Gateway
     |
Log / Request Pre-Processor
     |        \
Rule Engine   Ollama (LLama3 LLM)
     |           |
Merged Structured Insights
     |
Response back to UI
```

---

## 🛠️ Tech Stack & Why Chosen

### Backend

* **Python 3.10+** – Industry standard, excellent AI ecosystem
* **FastAPI** – High-performance, async-ready, production-grade APIs
* **Pydantic** – Strong data validation and schema enforcement

### AI / LLM

* **Ollama (LLaMA 3)** –

  * Runs fully **offline**
  * No API cost
  * Demonstrates real LLM integration skills

### Frontend

* **React.js** – Most in-demand frontend framework
* **Axios** – Clean API communication

### DevOps / Tooling

* **Docker** – Reproducible & scalable deployment
* **Git & GitHub** – Version control and collaboration

✅ This stack mirrors **real SaaS company architecture** used in Bangalore startups and MNCs.

---

## ⚙️ Step-by-Step Setup Guide

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

### 2️⃣ Backend Setup

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3️⃣ Install & Run Ollama

```bash
# Install Ollama (Linux/Mac)
curl -fsSL https://ollama.com/install.sh | sh

# Pull LLaMA 3 model
ollama pull llama3

# Start Ollama server
ollama serve
```

### 4️⃣ Start FastAPI Server

```bash
uvicorn main:app --reload
```

API will be available at:

```
http://127.0.0.1:8000
```

Swagger Docs:

```
http://127.0.0.1:8000/docs
```

---

### 5️⃣ Frontend Setup

```bash
cd frontend
npm install
npm start
```

Frontend runs at:

```
http://localhost:3000
```

---


## 👨‍💻 My Individual Contributions

* Designed **end-to-end SaaS architecture** from scratch
* Built **FastAPI backend** with clean routing & validation
* Integrated **local LLM (Ollama + LLaMA3)** for AI responses
* Implemented **rule engine + AI hybrid decision flow**
* Created **React UI** for real-time interaction
* Containerized services using **Docker**
* Wrote production-level **README & setup documentation**

---

## 🎯 Why This Project Stands Out

✅ Uses **real AI (LLM)**, not mock logic
✅ No paid APIs – fully local & cost-free
✅ SaaS-style architecture interviewers expect
✅ Clear separation of concerns
✅ Ready to scale and extend

---

## 📌 Future Enhancements

* Authentication (JWT)
* Multi-user support
* Database integration (PostgreSQL)
* Model switching (Mistral, Gemma)
* Cloud deployment (AWS / GCP)

---

## 📞 Contact

**Divith Raju**
🎓 B.Tech 
📍 Bangalore, India
🔗 GitHub: [https://github.com/divithraju](https://github.com/divithraju)

---

