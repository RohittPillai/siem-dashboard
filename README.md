# 🛡️ SIEM Dashboard – Real-Time Threat Detection & Log Analysis

A full-stack Security Information and Event Management (SIEM) platform built using Python (Flask), MongoDB, and Next.js. This dashboard ingests logs, detects threats using custom logic, and visualizes alerts in real time with a modern UI.

---

## 🎯 Project Overview

This project simulates how a SIEM works by:
- Accepting logs from external sources
- Detecting potential security threats (e.g., brute-force, port scanning, suspicious IPs)
- Saving them in a database
- Displaying insights on an interactive frontend dashboard

---

## 🚀 Features

- 📥 Log ingestion via REST API
- 💾 MongoDB for storing logs
- 🔍 Threat detection logic (custom rules)
- 📊 Real-time chart visualization (Next.js + Recharts)
- 🧠 GeoIP & blacklisted IP detection
- ⚙️ Custom detection rule engine (JSON-based)
- 🌗 Dark mode support
- 🔔 Email/Slack alerts
- 🧭 Map view for IP origins
- 🔒 User authentication (planned)
- 🐳 Dockerized infrastructure

---

## 🧱 Tech Stack

| Layer       | Technology                                |
|-------------|--------------------------------------------|
| Frontend    | Next.js (React), Tailwind CSS, Recharts   |
| Backend     | Python, Flask                             |
| Database    | MongoDB (via Docker)                      |
| DevOps      | Docker, Docker Compose                    |
| Extras      | AbuseIPDB, ip-api, SendGrid, Slack Webhooks|

---

## 📦 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/rohittpillai/siem-dashboard.git
cd siem-dashboard
```

### 2. Start backend (Flask + MongoDB)
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

###3. Start frontend (Next.js)
```bash
cd ../frontend
npm install
npm run dev
```

###4. Start MongoDB using Docker
```bash
docker run -d -p 27017:27017 --name siem-mongo mongo
```

## 📡 API Endpoints

| Method | Route         | Description                       |
|--------|---------------|-----------------------------------|
| GET    | `/`           | API health check                  |
| POST   | `/ingest-log` | Send JSON log data for processing |

---

## 🧠 Learning Goals

- Understand how SIEM tools ingest, analyze, and respond to security data  
- Build a full-stack app with security and observability in mind  
- Integrate third-party threat intelligence APIs  
- Deploy a scalable and modular architecture  

---

## 🗺️ Roadmap

- [ ] Custom Rule Editor in UI  
- [ ] Exportable incident reports (PDF)  
- [ ] Admin control panel  
- [ ] Multi-user auth system  
- [ ] WebSocket-based live alert updates  
- [ ] Hosted deployment (Vercel + Fly.io or Render)  

---

## 👨‍💻 Author

**Rohit Pillai**  
[GitHub](https://github.com/rohittpillai)

---

## 📃 License

This project is licensed under the MIT License.

> ⭐ Star this repo if you find it useful or inspiring!




