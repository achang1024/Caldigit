import os
import requests
from bs4 import BeautifulSoup

url = "https://www.caldigit.com/macos-ventura-and-usb-thunderbolt-device-security"
response = requests.get(url)
web_content = response.content

# Parse webpage content
soup = BeautifulSoup(web_content, "html.parser")

# Extract all text from the webpage
text_content = soup.get_text()

# Define the directory and file path
directory = "Caldigit/Knowledge Base"
file_path = os.path.join(directory, "caldigit_webpage.txt")

# Ensure the directory exists
os.makedirs(directory, exist_ok=True)

# Save the extracted text to a txt file
with open(file_path, "w", encoding="utf-8") as file:
    file.write(text_content)

print(f"Webpage content saved to {file_path}")
