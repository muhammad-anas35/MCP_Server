import requests

url= "http://127.0.0.1:8000/mcp"

headers = {
    "Accept": "application/json, text/event-stream",
}

body = {
    "jsonrpc": "2.0",
    "method": "tools/call",
    "id": 1,
    "params": {
        "name":"get_current_date",
        "arguments": {},
    },
   # "params": {
   #    "name":"get_current_weather",
   #   "arguments": {
   #      "city": "tokyo"
   # },
   # },
}

response = requests.post(url, headers=headers, json=body)

for line in response.iter_lines():
    if line:
        print(line)