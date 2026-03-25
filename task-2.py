import csv
import requests

#Extract file name
CSV_FILENAME = "Task 2 - Intern.csv"

def fetch_url_status(url):
    """Makes a GET request and returns the status code of the URL plus a specific error string."""
    try:
        response = requests.get(url, timeout=5)
        return response.status_code
    except requests.exceptions.Timeout:
        return "Timeout"
    except requests.exceptions.ConnectionError:
        return "Connection Error"
    except requests.exceptions.RequestException:
        return "Error"


if __name__ == "__main__":
    with open(CSV_FILENAME, newline="", encoding="utf-8") as file:
        reader = csv.reader(file)

        for row in reader:
            url = row[0].strip()
            status = fetch_url_status(url)
            print(f"({status}) {url}")


