# Phishing Email Detection

This project implements a phishing email detection system using rule-based logic and design patterns. The system detects phishing emails based on predefined rules, such as checking for suspicious links, sender addresses, and urgent language.

## Project Structure
```
phishing_email_detector/
│
├── detector/
│   ├── __init__.py
│   ├── base_rule.py
│   ├── suspicious_links_rule.py
│   ├── sender_address_rule.py
│   ├── urgent_language_rule.py
│   └── rule_factory.py
│
├── config/
│   ├── __init__.py
│   └── settings.py
│
├── main.py
└── README.md
```

## Requirements
- Python 3.x

## How to Run
1. Clone the repository.
2. Navigate to the project directory.
3. Run `python main.py`.

The script will process a sample email and print whether phishing is detected based on the specified rules.
