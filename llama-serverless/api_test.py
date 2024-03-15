import os
import requests

# Function to load environment variables from a .env file
def load_env_variables(filepath='.env'):
    with open(filepath) as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith('#'):
                key, value = line.split('=', 1)
                os.environ[key] = value

# Attempt to load environment variables; silently ignore if .env file is not found
if os.path.exists('.env'):
    load_env_variables('.env')

# Use environment variables for sensitive information
endpoint_id = os.getenv('ENDPOINT_ID')
api_key = os.getenv('API_KEY')

# Setup API details
url = f"https://api.runpod.ai/v2/{endpoint_id}"
headers = {"Authorization": api_key}
payload = {"input": {"prompt": "Me: Hello, what is your purpose?\nAI:"}}

# Synchronous API call
response_sync = requests.post(f"{url}/runsync", json=payload, headers=headers)
print(response_sync.json())

# Asynchronous API call
response_async = requests.post(f"{url}/run", json=payload, headers=headers)
async_id = response_async.json().get("id")

# Retrieve asynchronous call result
if async_id:
    response_result = requests.get(f"{url}/status/{async_id}", headers=headers)
    print(response_result.json())
