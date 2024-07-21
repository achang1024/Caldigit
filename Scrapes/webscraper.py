import os
import requests
from bs4 import BeautifulSoup

url = "https://www.caldigit.com/macos-ventura-and-usb-thunderbolt-device-security"
response = requests.get(url)
web_content = response.content


# Extract all text from the webpage

#Inspect the Webpage: Use your browser's developer tools (right-click on the page and select "Inspect" or press Ctrl+Shift+I) to find the specific HTML elements
# that contain the article text. Look for common tags like <p>, <div>, or <article>

if response.status_code == 200:
    print("Page retrieved successfully")
    soup = BeautifulSoup(response.content, 'html.parser')
    # Extract main content 
    article_content = soup.find()
    if article_content:
        # Extract all paragraph texts within the main article content
        paragraphs = article_content.find_all('p')

        article_text = '\n\n'.join([p.get_text() for p in paragraphs])

        # Print the extracted text
        print(article_text)
    else:
        print("Article content not found.")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
# Define the directory and file path
directory = "Caldigit/Knowledge Base"
file_path = os.path.join(directory, "caldigit_webpage.txt")

# Ensure the directory exists
os.makedirs(directory, exist_ok=True)

# Save the extracted text to a txt file
with open(file_path, "w", encoding="utf-8") as file:
    file.write(article_text)

print(f"Webpage content saved to {file_path}")
