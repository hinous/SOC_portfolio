#   ___ _ __ | |_ _ __ ___   _ __  _   _ 
 / _ \ '_ \| __| '__/ _ \ | '_ \| | | |
|  __/ | | | |_| | | (_) || |_) | |_| |
 \___|_| |_|\__|_|  \___(_) .__/ \__, |
                          |_|    |___/ 
luishinojosa@Laptop-de-Luis Documents % 
# Password Entropy Analyzer & Strength Tester 🔐

## Overview
This project is a Python-based security tool designed to evaluate password strength. Rather than relying solely on basic length and character requirements, this tool calculates the **mathematical entropy** (in bits) of a password and cross-references it against known breached password lists (e.g., `rockyou.txt`) to simulate a realistic threat assessment.

## Key Features
* **Entropy Calculation:** Uses mathematical entropy principles to determine resistance against brute-force attacks based on the character pool size (lowercase, uppercase, digits, symbols) and password length.
* **Breach Dictionary Check:** Cross-references inputs against a local wordlist to flag compromised passwords instantly.
* **O(1) Time Complexity Lookups:** Utilizes Python `set` structures for loading wordlists, ensuring lightning-fast lookups even with massive datasets.
* **Shoulder-Surfing Protection:** Implements the `getpass` module to securely handle standard input without echoing characters to the terminal.
* **Actionable Feedback:** Provides specific recommendations to users on how to meet secure password policies.

## SOC & Blue Team Relevance
As a SOC Analyst, understanding how threat actors exploit weak credentials is vital. This tool demonstrates:
* Knowledge of **Identity and Access Management (IAM)** best practices.
* Understanding of **brute-force and dictionary attack** mitigation strategies.
* Secure scripting practices (handling sensitive inputs, memory-efficient data structures, exception handling).

## Prerequisites
* Python 3.x

## Usage
1. Clone the repository to your local machine.
2. (Optional) Place a `rockyou.txt` dictionary file in the root directory. *Note: Ensure this file is added to your `.gitignore` to prevent uploading large files to GitHub.*
3. Run the script via terminal:
   ```bash
     python3 password_entropy_analyzer.py
4.   Enter passwords securely when prompted to receive an entropy score and security rating.

## Disclaimer
## This tool is intended for educational purposes and personal security auditing.
