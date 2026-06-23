# ⌨️ KeyScribe - Terminal Key Logger

## 📖 Overview

KeyScribe is a Python-based terminal key logging simulator that captures user-entered text during program execution after obtaining explicit user consent. It demonstrates key logging concepts in a safe and controlled environment for educational purposes, cybersecurity awareness, and ethical security learning.

This project was developed as part of the Prodigy InfoTech Cyber Security Internship Program.

---

## Key Logging Concept

Key logging refers to the process of recording user input for monitoring, auditing, troubleshooting, or educational purposes.

While real-world keyloggers may capture system-wide keystrokes and operate in the background, KeyScribe is designed as an ethical learning tool that:

* Requires explicit user consent before logging begins
* Records only text entered within the program
* Does not run in the background
* Does not capture system-wide keystrokes
* Operates entirely within its own terminal session

KeyScribe demonstrates how logging mechanisms work while maintaining user privacy and ethical security practices.

---

## ✨ Features

### User Consent Verification

* Requests permission before logging starts
* Prevents logging without user approval

### Terminal Input Logging

* Records text entered within the program
* Captures user input line by line

### Timestamped Log Entries

* Adds date and time information to every log entry
* Maintains chronological records

### Log File Storage

* Saves captured input to a text file
* Preserves records between sessions

### Session-Based Operation

* Runs only while the program is active
* Stops logging when the user exits

### Ethical Design

* No background execution
* No system-wide keystroke capture
* Designed for educational purposes only

---

## 🛠️ Technologies Used

* Python
* File Handling
* Date and Time Management
* User Input Processing
* Logging Mechanisms

---

## 📂 Project Structure

```text
KeyScribe/
│
├── keylogger.py
└── key_logs.txt
```

---

## 🚀 How to Run

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/manigandanb02/PRODIGY_CS_04.git KeyScribe
```

### 2️⃣ Navigate to the Project Folder

```bash
cd KeyScribe
```

### 3️⃣ Run the Program

#### Windows

```bash
python keylogger.py
```

#### Linux (Ubuntu)

```bash
python3 keylogger.py
```

---

## Demo Video

Watch the project demonstration on LinkedIn:

[LinkedIn Demo Video](https://www.linkedin.com/posts/manigandanb02_prodigyinfotech-cybersecurity-python-ugcPost-7475193336207712256-byR_/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFJ8ul4BQ42d707c6KxMYCd3agIPNUqbyhA)

---

## 📚 Learning Outcomes

Through this project, I learned:

* Fundamentals of logging mechanisms
* Ethical considerations of key logging
* User consent implementation
* File handling in Python
* Timestamp management
* Input processing techniques
* Secure and responsible software design
* Command-line application development

---

## ⚠️ Disclaimer

This project is developed for educational purposes and cybersecurity awareness.

KeyScribe is an ethical terminal-based key logging simulator that records only user-entered text within its own execution environment after obtaining explicit consent. It does not perform background monitoring, system-wide keystroke capture, or any form of unauthorized data collection.
