

---

## 📖 Overview

This project simulates a simple Security Information and Event Management (SIEM) workflow by reading authentication logs, analyzing login attempts, and identifying potentially malicious activity such as repeated failed logins and possible brute-force attacks.

The project was built to strengthen Python fundamentals while applying them to a real cybersecurity use case.

---

## ✨ Features

* 📂 Parse authentication log files
* ❌ Count failed login attempts
* ✅ Count successful login attempts
* 🌐 Track failed login attempts by IP address
* 🚨 Detect suspicious IP addresses (3+ failed attempts)
* 🔥 Detect possible brute-force attacks (5+ failed attempts)
* 📊 Generate a structured security report
* 🧩 Modular project architecture

---

## 📁 Project Structure

```text
Security-Log-Analyzer/
│
├── main.py              # Runs the application
├── parser.py            # Parses authentication logs
├── detector.py          # Detects suspicious activity
├── report.py            # Generates the security report
├── logs/
│   └── auth.log         # Sample authentication log
└── README.md
```

---

## 🛠️ Technologies Used

* Python 3
* Dictionaries
* Lists
* Loops
* Functions
* File Handling
* Modular Programming

---

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/thesakhoyat-og/Security-Log-Analyzer.git
```

### Navigate to the project

```bash
cd Security-Log-Analyzer
```

### Run the project

```bash
python main.py
```

---

## 📄 Sample Output

```text
========================================
       SECURITY LOG ANALYZER REPORT
========================================

Summary
----------------------------------------
Failed Login Attempts     : 8
Successful Login Attempts : 2

========================================

Failed Login Attempts by IP Address
----------------------------------------
10.0.0.25 -> 5
10.0.0.18 -> 2
10.0.0.10 -> 1

========================================

Suspicious IP Addresses
----------------------------------------
10.0.0.25 -> 5

========================================

Possible Brute Force Attempts
----------------------------------------
10.0.0.25 -> 5

========================================
```

---

## 🎯 Learning Objectives

This project demonstrates practical use of:

* File handling
* Data parsing
* Dictionaries
* Conditional logic
* Iteration
* Modular programming
* Basic cybersecurity concepts
* Writing maintainable Python code

---

## 🔮 Future Improvements

* Export reports as PDF or CSV
* Add timestamp-based attack detection
* Detect repeated username attacks
* Interactive command-line interface
* Colorized terminal output
* Support multiple log formats
* Unit testing with `pytest`
* Logging and configuration support

---

## 👨‍💻 Author

Md Sakhoyat Hossain Siam



## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

Every starred repository makes one programmer slightly more motivated and one README feel less like it was written into the void.
