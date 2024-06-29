from youtube_transcript_api import YouTubeTranscriptApi


def download_transcript(video_id):
    try:
        # Fetch the transcript
        transcript = YouTubeTranscriptApi.get_transcript(video_id)


        # Print and save the transcript
        with open(f"{video_id}_transcript.txt", "w", encoding="utf-8") as file:
            for entry in transcript:
                line = f"{entry['text']} (starts at {entry['start']}s)\n"
                print(line)
                file.write(line)


        print("Transcript downloaded and saved successfully!")
    except Exception as e:
        print("An error occurred:", e)


video_id = 'ochbv7m1Cj8&list=PLhIVjSB4u_gz4f2XVlBzIuB5FAInDPII6&ab_channel=CalDigit'
download_transcript(video_id)




