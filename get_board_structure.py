
import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("MONDAY_API_TOKEN")
URL = "https://api.monday.com/v2"

BOARD_ID = 5030779993  # Replace with your board ID

query = """
query {
    boards(ids: [BOARD_ID_PLACEHOLDER]) {
        id
        name

        groups {
            id
            title
        }

        columns {
            id
            title
            type
        }
    }
}
"""

query = query.replace(
    "BOARD_ID_PLACEHOLDER",
    str(BOARD_ID),
)

response = requests.post(
    URL,
    json={"query": query},
    headers={
        "Authorization": API_TOKEN,
        "Content-Type": "application/json",
    },
)

print(response.json())