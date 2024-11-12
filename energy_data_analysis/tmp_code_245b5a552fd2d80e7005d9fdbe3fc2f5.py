import requests
from bs4 import BeautifulSoup

# Search for Chicago Energy data for the years 2020-2024
url = "https://www.chicago.gov/city/en/depts/dhcd/supp_info/chicago_energy_data.html"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
links = soup.find_all('a', href=True)

# Print all links found on the page
for link in links:
    print(link['href'])