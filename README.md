# 🚨 Avalok AI Agentic Surveillance Platform

**Tech Stack:** Vertex AI Vision, Gemini 2.5 Pro, Google Cloud Platform (GCP), FastAPI, Docker, Cloud Run, Firestore, Firebase, DeepSORT, Hungarian Algorithm, Retrieval-Augmented Generation (RAG), ADK (Agent Development Kit)

---

## 🧠 Project Overview

**Avalok AI Agent** is a multi-agent, agentic AI system designed for **real-time surveillance** and **incident response** in large-scale public areas (e.g., festivals, rallies, airports). It leverages drone-based video and audio feeds to detect critical events and autonomously dispatch response units.

This intelligent system is capable of:

- 🔥 Fire and motion anomaly detection  
- 😱 Panic detection via audio and sentiment analysis  
- 🧍 Lost & Found person matching via Gemini Vision  
- 🚁 Drone dispatch simulation and tracking  
- 🌐 Real-time dashboard integration for zone-wise updates

---

## 🧩 Core Features

| Agent Name              | Functionality |
|-------------------------|---------------|
| 🔍 Lost & Found Matcher | Visual identity matching using Gemini 2.5 Pro |
| 📊 Crowd Flow Forecaster | Forecast crowd density via keyframe analysis |
| 🚨 Incident Detector     | Fire, collapse, or suspicious motion detection |
| 😓 Sentiment Analyzer    | Audio-based emotional stress recognition |
| 🚁 Auto-Drone Dispatcher | Assign blind-spot drone coverage |
| 🧠 LiveUpdate Synthesizer| Summarizes alerts from all agents |
| 👮 Staff Auto-Dispatcher | Routes staff using Firestore + Maps API |

All agents are built using Google’s **ADK toolkit**, with support from **RAG-based LLM reasoning** for context-aware decisions.

---

## 🛠️ System Architecture

- **Ingestion Layer**: Drone videos (30–60 sec clips) and audio pushed to Cloud Storage
- **Frame Selection**: DeepSORT + Hungarian algorithm used for keyframe detection
- **Pipeline Coordination**: Vertex AI Agents process clips and store results in Firestore
- **LLM Reasoning**: Gemini 2.5 Pro (via ADK) supports multi-modal input reasoning
- **Dashboard**: Firebase + Maps API for real-time monitoring and response

---

## ⚙️ Technologies Used

- **Languages**: Python (FastAPI), JavaScript (Frontend), SQL
- **AI Tools**: Vertex AI Vision, Gemini 2.5 Pro, Retrieval-Augmented Generation (RAG), DeepSORT
- **Cloud Infra**: GCP (Cloud Run, Cloud Functions, IAM, Cloud Storage, Firestore, Cloud Build)
- **DevOps**: Docker, Git, Google Cloud Build
- **Other APIs**: Google Maps API, Firebase Auth & Emulator Suite

---

## 🚀 Deployment

- Microservices containerized using Docker
- Deployed to Google Cloud Run via `gcloud builds submit`
- Uses Firestore for low-latency event logging and Firebase for secure frontend hosting

---

## 📈 Success Metrics

- ⏱ Sub-5 second average response latency
- 📍 Accurate location-based alerts with heatmaps
- 🧠 LLM-supported alert synthesis and decision making
- 🚓 Real-time automated drone/staff dispatch visualization

---

## 🤖 Future Scope

- Integrate body pose tracking for advanced behavioral analysis  
- Expand agent logic to support multilingual speech cues  
- Add reinforcement learning for adaptive response modeling

---

ed under the [MIT License](LICENSE).
