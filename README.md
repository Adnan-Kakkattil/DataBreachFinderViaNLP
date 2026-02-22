# Social Media Monitoring for Data Leakage
### Web Scraping, NLP, and Public Data Analysis

## 🛡️ Overview
In the digital era, organizations face significant risks from data leakage on social media. This project is an automated system developed for **Social Media Monitoring for Data Leakage**. It leverages **Web Scraping**, **Natural Language Processing (NLP)**, and **Public Data Analysis** to proactively detect sensitive or confidential information shared across public platforms.

## 🚀 Key Features
- **Real-time Monitoring**: Continuously scans (simulated) social media feeds for potential threats.
- **NLP Detection Engine**: Uses context-aware patterns to identify:
  - 📧 Email addresses
  - 🔑 API Keys and Auth Tokens
  - 🔓 Passwords and Credentials
  - 🆔 Personally Identifiable Information (SSN, etc.)
  - 💳 Credit Card details
- **Automated Alerts**: Real-time dashboard updates with severity levels (High/Medium).
- **Interactive Dashboard**: Premium glassmorphism UI for monitoring and manual scanning.

## 🛠️ Technology Stack
- **Backend**: Python 3.x, FastAPI (Asynchronous Framework)
- **NLP**: Regular Expressions & Contextual Analysis
- **Frontend**: HTML5, Vanilla CSS (Glassmorphism), JavaScript (ES6+)
- **Server**: Uvicorn

## 📁 Project Structure
```text
DataBreachFinderViaNLP/
├── engine/
│   ├── nlp_engine.py         # Detection logic and patterns
│   └── scraper_simulator.py  # Mock social media data generator
├── static/
│   ├── index.html            # Dashboard UI
│   ├── style.css             # Premium styling
│   └── app.js                # Frontend logic & API integration
├── main.py                   # FastAPI server entry point
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

## ⚙️ Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd DataBreachFinderViaNLP
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python main.py
   ```

4. **Access the Dashboard**:
   Open your browser and navigate to `http://localhost:8000`

## 📊 Verification
The system has been verified using automated browser testing. It successfully detects leaked entities in real-time and provides high-visibility alerts on the management dashboard.

---
*Developed as a proactive cybersecurity solution to protect digital assets across public platforms.*