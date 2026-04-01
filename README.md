# 🚀 DarkSqli Pro CLI Scanner

**DarkSqli Pro** is a powerful SQL Injection vulnerability scanner designed for professional web security testing.  
It helps detect SQL injection points (boolean, error‑based, time‑based) in web applications, with smart parameter parsing + async scanning + anomaly detection.

> ⚠️ **Use this tool responsibly. Only scan applications you own, are authorized to test, or are part of a bug bounty program. Unauthorized scanning is illegal.**

---

## 📦 Features

🔥 **Async ultra-fast scanning**  
🧠 **Multi‑parameter detection** (supports URLs with multiple params)  
🔍 **Boolean / Error / Time‑based SQLi detection**  
🤖 **ML‑based anomaly detection**  
🧬 **Database fingerprinting** (MySQL, PostgreSQL, Oracle, SQLite)  
🔐 **Payload encoding for WAF bypass simulation**  
📊 **Confidence scoring (vuln likelihood)**  
📄 **Dark HTML report** with classification and confidence  
🛠️ Clean modular architecture for easy extension  

---

## 🧰 Installation

Before using DarkSqli Pro, you need:

✔️ Python 3.7+  
✔️ `aiohttp`  
✔️ `scikit‑learn`

### 🐍 Python Setup

```bash
git clone https://github.com/yourusername/DarkSqli.git
cd DarkSqli

python3 -m venv venv
source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt
```
Run app.py 
```bash
python app.py
```

After scan, open:
```bash
report.html
```
📄 Report Output

---

The scanner produces a dark themed HTML report with:

✅ Parameter tested
✅ Payload used
✅ Vulnerability status
✅ Database detected
✅ ML‑based anomaly flag
✅ Confidence score

---

🧠 How It Works
Parses URL parameters
Sends baseline request
Injects smart payloads into each param
Measures response length & timing
Uses ML to detect anomalies
Fingerprints DB error strings
Generates HTML report
🛡️ Important Safety Notice
---

DarkSqli Pro is a security testing tool — not an exploitation suite.
Always follow legal & ethical guidelines:

✔ Get permission before scanning
✔ Don’t attempt exploitation without authorization
✔ Bug bounty programs require scope validation

---

📁 Project Structure
```bash
DarkSqli/
│── app.py
│── scanner/
│   ├── __init__.py
│   ├── async_scan.py
│   ├── core.py
│   ├── payloads.py
│   ├── fingerprint.py
│   ├── ml_model.py
│   ├── encoder.py
│   └── utils.py
│── report/
│   ├── __init__.py
│   └── report_generator.py
├── assets/
│   ├── __init__.py
│   └── loader.py
└── requirements.txt
```
---

👥 Contributing

Contributions welcomed!
Open issues or pull requests for:

✅ New detection methods
✅ More payload categories
✅ Improved ML dataset & models
✅ Plugin architecture

---

📜 License

MIT License

---
## Author

DarkSqlinjection Team – Advanced Web Vulnerability Scanner Project
GitHub: https://github.com/csejobaer/DarkSqli

# 📜 License

This project is for **educational and authorized security testing purposes only**.
