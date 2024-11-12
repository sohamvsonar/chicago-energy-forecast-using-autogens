# filename: check_chicago_energy_data.py
import requests

# Step 1: Download the data
url = "https://example.com/chicago_energy_data.csv"  # Replace with actual URL
response = requests.get(url)

# Step 2: Print the raw content of the response
print(response.text[:500])  # Print the first 500 characters to check the data format