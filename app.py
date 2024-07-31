from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import openai
import os
import logging

# Load environment variables from a .env file
load_dotenv()

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Set your OpenAI API key from environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')

app.logger.info(f"OpenAI API Key: {openai.api_key}")

# Define keyword triggers and responses
keyword_responses = {
    "ts4 port broken": "I'm sorry to hear that your TS4 port is broken. Could you please provide more details about the issue? For instance, which port is not working and what device are you trying to connect?",
    "usb-c port not working": "Thank you for the details. Let's try some troubleshooting steps. Have you tried using a different USB-C cable or port on your laptop to see if the issue persists?",
    "hello": "Hello! How can I assist you today?",
    "hi": "Hi there! How can I help you?"
}

@app.route('/')
def home():
    # Render the index.html template when accessing the root URL
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    # Retrieve the user message from the request JSON data
    user_message = request.json.get('message')
    
    if not user_message:
        # Log and return an error response if no message is provided
        app.logger.error("No message provided")
        return jsonify({'error': 'No message provided'}), 400
    
    # Convert user message to lower case for case insensitive keyword matching
    user_message_lower = user_message.lower()
    
    # Check for keyword responses
    for keyword, response in keyword_responses.items():
        if keyword in user_message_lower:
            app.logger.info(f"User message: {user_message}")
            app.logger.info(f"Keyword response: {response}")
            return jsonify({'message': response})
    
    # Generate a response from the OpenAI API using the fine-tuned model if no keyword matches
    try:
        response = openai.Completion.create(
            model="ft:davinci-002:caldigit-test-chatbot:cal-bot:9oyV5jTW",  # Use the appropriate model name
            prompt=f"User: {user_message}\nChatbot:",
            max_tokens=100,
            temperature=0.1,  # Adjust the temperature for more conversational responses
            stop=["User:", "Chatbot:"]  # Ensure the response stops at the appropriate place
        )
        # Extract the chatbot's message from the response
        chatbot_message = response['choices'][0]['text'].strip()
        app.logger.info(f"User message: {user_message}")
        app.logger.info(f"Chatbot response: {chatbot_message}")
        return jsonify({'message': chatbot_message})
    
    except openai.error.OpenAIError as oe:
        # Log and return OpenAI API errors
        app.logger.error(f"OpenAI API error: {oe}")
        return jsonify({'error': 'OpenAI API error'}), 500
    
    except Exception as e:
        # Log and return any other errors
        app.logger.error(f"Error: {e}")
        return jsonify({'error': 'Internal server error'}), 500

# Route to test if the API key is working
@app.route('/test-api')
def test_api():
    try:
        # Generate a response from the OpenAI API using a test message
        response = openai.Completion.create(
            model="ft:gpt-3.5-turbo-1106:caldigit-test-chatbot:cal-bot:9q6vR10M",  # Use the appropriate model name
            prompt="User: Hello, how are you?\nChatbot:",
            max_tokens=150
        )
        # Return the chatbot's message from the test response
        chatbot_message = response['choices'][0]['text'].strip()
        app.logger.info("API key test successful")
        return jsonify({'message': chatbot_message})
    
    except openai.error.OpenAIError as oe:
        # Log and return OpenAI API errors
        app.logger.error(f"OpenAI API error: {oe}")
        return jsonify({'error': 'OpenAI API error'}), 500
    
    except Exception as e:
        # Log and return any other errors
        app.logger.error(f"Error: {e}")
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Run the Flask application in debug mode
    app.run(debug=True)
