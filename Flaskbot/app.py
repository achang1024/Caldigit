from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import openai
import os

# Load environment variables from a .env file
load_dotenv()

app = Flask(__name__)

# Set your OpenAI API key from environment variables
openai.api_key = os.getenv('MY_SECRET_KEY')

@app.route('/')
def home():
    # Render the index.html template when accessing the root URL
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    # Retrieve the user message from the request JSON data
    user_message = request.json.get('message')
    
    if not user_message:
        # If no message is provided, return an error response
        return jsonify({'error': 'No message provided'}), 400
    
    # Generate a response from the OpenAI API using the gpt-3.5-turbo model
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use the appropriate model name
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}       
            ]
        )
        # Extract the chatbot's message from the response
        chatbot_message = response['choices'][0]['message']['content'].strip()
        return jsonify({'message': chatbot_message})
    
    except Exception as e:
        # If an error occurs, return the error message
        return jsonify({'error': str(e)}), 500

# Route to test if the API key is working
@app.route('/test-api')
def test_api():
    try:
        # Generate a response from the OpenAI API using a test message
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use the appropriate model name
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Hello, how are you?"}
            ]
        )
        # Return the chatbot's message from the test response
        chatbot_message = response['choices'][0]['message']['content'].strip()
        return jsonify({'message': chatbot_message})
    
    except Exception as e:
        # If an error occurs, return the error message
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application in debug mode
    app.run(debug=True)
