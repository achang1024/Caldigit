import json

# Load the JSONL file
input_file_path = 'display_konwledgebase_separate.jsonl'
messages_list = []

with open(input_file_path, 'r', encoding='utf-8') as file:
    for line in file:
        try:
            messages_list.append(json.loads(line))
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            continue

# Convert to the desired format and write to a new JSONL file
output_file_path = 'converted_messages.jsonl'

with open(output_file_path, 'w', encoding='utf-8') as outfile:
    for message in messages_list:
        prompt = message.get("prompt", "")
        completion = message.get("completion", "")
        if prompt and completion:
            conversation = {
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    },
                    {
                        "role": "assistant",
                        "content": completion
                    }
                ]
            }
            outfile.write(json.dumps(conversation) + '\n')
        else:
            print(f"Skipping empty message: {message}")

print(f"Converted messages saved to {output_file_path}")
