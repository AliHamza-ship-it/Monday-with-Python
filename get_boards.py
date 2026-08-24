import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("MONDAY_API_TOKEN")
URL = "https://api.monday.com/v2"

query = """
query {
    boards(limit: 20) {
        id
        name
    }
}
"""

response = requests.post(
    URL,
    json={"query": query},
    headers={
        "Authorization": API_TOKEN,
        "Content-Type": "application/json",
    },
)

print(response.status_code)
print(response.json())