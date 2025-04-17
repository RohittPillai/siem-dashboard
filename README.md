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
