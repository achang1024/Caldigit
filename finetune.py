import openai
import os
import json
from dotenv import load_dotenv
import time

# Load environment variables from a .env file
load_dotenv()

# Set your OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Upload the training file
training_file_path = 'training_data_prepared.jsonl'

# Ensure the file exists
if not os.path.exists(training_file_path):
    raise FileNotFoundError(f"Training data file {training_file_path} not found.")

# Create a file for the fine-tuning job
with open(training_file_path, 'rb') as f:
    training_file = openai.File.create(file=f, purpose='fine-tune')

print(f"Uploaded training file ID: {training_file['id']}")

# Fine-tune the model using the updated endpoint
fine_tune_response = openai.FineTune.create(
    training_file=training_file['id'],
    model="davinci"  # Base model for fine-tuning, adjust if necessary
)

print(f"Fine-tune job response: {fine_tune_response}")

# Monitor the fine-tuning job
status = fine_tune_response['status']
job_id = fine_tune_response['id']

while status != 'succeeded':
    fine_tune_status = openai.FineTune.retrieve(id=job_id)
    status = fine_tune_status['status']
    print(f"Fine-tune job status: {status}")
    if status in ['failed', 'cancelled']:
        raise RuntimeError(f"Fine-tune job failed or was cancelled with status: {status}")
    time.sleep(30)  # Check the status every 30 seconds

# Once fine-tuning is complete, print the fine-tuned model ID
print(f"Fine-tuned model ID: {fine_tune_status['fine_tuned_model']}")
