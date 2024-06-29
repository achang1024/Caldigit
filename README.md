# CalDigit Summer Internship Project

## Overview

This project is part of the CalDigit Summer Internship program, focusing on enhancing customer support through automation and AI. Our goal is to integrate a chatbot within Zendesk using OpenAI's GPT models to handle common customer queries efficiently. The project also involves culling data from CalDigit's Knowledge Base and downloading YouTube transcripts to train the model.

## Key Components

### Zendesk Integration

- **Objective**: Implement a basic chatbot to answer customer queries within the Zendesk environment using OpenAI's API.
- **Technologies Used**: OpenAI API, Zendesk API.
- **Main Tasks**:
  1. Set up and configure access to OpenAI's API.
  2. Integrate chatbot responses via the Zendesk API.
  3. Train the chatbot to handle common customer queries.
  4. Conduct thorough testing to ensure reliable functionality.

### Knowledge Base Data Culling

- **Objective**: Extract relevant articles and information from CalDigit.com to provide data for training the AI model.
- **Technologies Used**: Python, BeautifulSoup for web scraping.
- **Process**:
  1. Identify target URLs within CalDigit’s Knowledge Base.
  2. Scrape the content using Python scripts.
  3. Format and prepare data for AI model training.

### YouTube Transcript Download

- **Objective**: Automate the downloading of YouTube video transcripts from the CalDigit channel to use as training data.
- **Technologies Used**: `youtube_transcript_api`, Python.
- **Process**:
  1. Fetch transcripts using the YouTube Transcript API.
  2. Save transcripts locally for further processing and model training.

## Getting Started

### Prerequisites

- Python 3.8 or later.
- Access to OpenAI and Zendesk APIs.
- Install necessary Python libraries:
  ```bash
  pip install requests beautifulsoup4 youtube_transcript_api
