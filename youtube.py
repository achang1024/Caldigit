"""
This Python script uses the youtube_transcript_api to download and save the transcript of a YouTube video.
It fetches the transcript based on the video ID and saves it to a text file. Each line in the file includes
a segment of the transcript along with its starting time in the video, formatted for easy reading and reference.
"""

from youtube_transcript_api import YouTubeTranscriptApi
import requests
from bs4 import BeautifulSoup
import os

def get_video_title(video_id):
    url = f"https://www.youtube.com/watch?v={video_id}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.find('meta', property='og:title')['content']
    return title

def download_transcript(video_id):
    try:
        # Fetch the transcript
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        
        # Fetch the video title
        video_title = get_video_title(video_id)
        # Clean the title to use it as a filename
        safe_title = "".join([c if c.isalnum() else "_" for c in video_title])

        # Define the directory and file path
        directory = "Caldigit/YouTube Scripts"
        
        file_path = os.path.join(directory, f"{safe_title}_transcript.txt")

        # Ensure the directory exists
        os.makedirs(directory, exist_ok=True)

        # Print and save the transcript
        with open(file_path, "w", encoding="utf-8") as file:
            for entry in transcript:
                line = f"{entry['text']} (starts at {entry['start']}s)\n"
                print(line)
                file.write(line)

        print(f"Transcript downloaded and saved as {file_path}")
    except Exception as e:
        print("An error occurred:", e)

video_id = 'ochbv7m1Cj8&list=PLhIVjSB4u_gz4f2XVlBzIuB5FAInDPII6&ab_channel=CalDigit'
download_transcript(video_id)
