import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("MONDAY_API_TOKEN")
URL = "https://api.monday.com/v2"

BOARD_ID = 5030779993
GROUP_ID = "topics"

column_values = {
    "status": {
        "label": "Working on it"
    },
    "priority": {
        "label": "High"
    }
}

query = """
mutation (
    $board_id: ID!,
    $group_id: String!,
    $item_name: String!,
    $column_values: JSON!
) {
    create_item(
        board_id: $board_id,
        group_id: $group_id,
        item_name: $item_name,
        column_values: $column_values
    ) {
        id
        name
    }
}
"""

variables = {
    "board_id": str(BOARD_ID),
    "group_id": GROUP_ID,
    "item_name": "Learn Monday API",
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