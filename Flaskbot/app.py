from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv  # Import for loading environment variables from a .env file
import openai  # Import OpenAI library for GPT-3.5-turbo model
import os  # Import os library to interact with environment variables

# Load environment variables from a .env file
load_dotenv()

app = Flask(__name__)  # Create a Flask application instance

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
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Specify the model to use
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},  # System message to set the assistant's behavior
            {"role": "user", "content": user_message}  # User message with the content from the request
        ]
    )
    
    # Extract the chatbot's message from the response
    chatbot_message = response['choices'][0]['message']['content'].strip()
    
    # Return the chatbot's message as a JSON response
    return jsonify({'message': chatbot_message})

# Route to test if the API key is working
@app.route('/test-api')
def test_api():
    try:
        # Generate a response from the OpenAI API using a test message
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Specify the model to use
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},  # System message to set the assistant's behavior
                {"role": "user", "content": "Hello, how are you?"}  # Test user message
            ]
        )
        # Return the chatbot's message from the test response
        return jsonify({'message': response['choices'][0]['message']['content'].strip()})
    except Exception as e:
        # If an error occurs, return the error message
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application in debug mode
    app.run(debug=True)
