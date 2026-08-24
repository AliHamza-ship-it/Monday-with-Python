import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("MONDAY_API_TOKEN")
URL = "https://api.monday.com/v2"

BOARD_ID = 5030779993
ITEM_ID = 2840500329

column_values = {
    "status": {
        "label": "Done"
    }
}

query = """
mutation (
    $board_id: ID!,
    $item_id: ID!,
    $column_values: JSON!
) {
    change_multiple_column_values(
        board_id: $board_id,
        item_id: $item_id,
        column_values: $column_values
    ) {
        id
        name
    }
}
"""

variables = {
    "board_id": str(BOARD_ID),
    "item_id": str(ITEM_ID),
    "column_values": json.dumps(column_values),
}

response = requests.post(
    URL,
    json={
        "query": query,
        "variables": variables,
    },
    headers={
        "Authorization": API_TOKEN,
        "Content-Type": "application/json",
    },
)

print(response.json())