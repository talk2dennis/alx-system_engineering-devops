import requests

# Replace 'YOUR_API_KEY' and 'YOUR_APP_KEY' with your actual Datadog API and application keys
api_key =''
app_key =''

# Authenticate with the Datadog API
headers = {
    'Content-Type': 'application/json',
    'DD-API-KEY': api_key,
    'DD-APPLICATION-KEY': app_key
}

# Make a GET request to list dashboards
response = requests.get('https://api.datadoghq.com/api/v1/dashboard', headers=headers)

# Parse the response and extract the dashboard_id
if response.status_code == 200:
    dashboards = response.json()
    if dashboards:
        print(dashboards)
        # print("Dashboard ID:", dashboard_id)
    else:
        print("No dashboards found")
else:
    print("Failed to fetch dashboards. Status code:", response.status_code)
