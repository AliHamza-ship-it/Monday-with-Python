import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("MONDAY_API_TOKEN")
URL = "https://api.monday.com/v2"

BOARD_ID = 5030779993
GROUP_ID = "topics"

query = """
mutation {
    create_item(
        board_id: BOARD_ID_PLACEHOLDER,
        group_id: "GROUP_ID_PLACEHOLDER",
        item_name: "Task Created From Python"
    ) {
        id
        name
    }
}
"""

query = query.replace(
    "BOARD_ID_PLACEHOLDER",
    str(BOARD_ID),
).replace(
    "GROUP_ID_PLACEHOLDER",
    GROUP_ID,
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