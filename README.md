# Task 2 — URL Status Checker

Reads URLs from a CSV file and prints the HTTP status code for each one in this format:
(200) https://www.nytimes.com/1999/07/04/sports/women-s-world-cup-sissi-of-brazil-has-right-stuff-with-left-foot.html

## Usage

```bash
pip3 install requests
python3 task-2.py
```

Place Task 2 - Intern.csv in the same folder as the script.

Notes  
Uses csv.reader to parse the CSV and requests.head with a 5-second timeout for each URL.  
Handles specific errors: Timeout, ConnectionError, and a general RequestException fallback.
