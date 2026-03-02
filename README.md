# log-analysis-bruteforce-detection
📌 Overview

This project simulates a basic Security Operations Center (SOC) log monitoring system.
It analyzes authentication logs and detects potential brute-force login attempts based on repeated failed login attempts.

🚨 What Is a Brute-Force Attack?

A brute-force attack occurs when an attacker repeatedly attempts different password combinations to gain unauthorized access to an account. This typically results in multiple failed login attempts within a short period.

⚙ How This Script Works

Reads authentication log file (auth_log.txt)

Identifies failed login attempts

Counts failed attempts per user

Triggers alert if failed attempts exceed threshold (3 attempts)

🛠 Technologies Used

Python

File Handling

Dictionary-based counting logic

Threshold-based detection
