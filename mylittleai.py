import openai
import random
import string
import time

# Set up OpenAI API credentials
openai.api_key = '- '

# Function to generate a random prompt and ask the LLM
def generate_prompt():
    # Generate a random prompt dynamically
    prompt_length = random.randint(10, 30)
    prompt = ''.join(random.choices(string.ascii_letters + string.digits, k=prompt_length))

    # Ask the LLM for a response
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100  # Customize the number of tokens in the response
    )

    # Extract the generated answer from the API response
    answer = response.choices[0].text.strip()

    return prompt, answer

# Function to write prompt and answer to a Markdown file
def write_to_markdown(prompt, answer):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    filename = f"{timestamp.replace(':', '-')}.md"
    with open(filename, 'w') as file:
        file.write(f"Timestamp: {timestamp}\n\n")
        file.write(f'## Prompt:\n{prompt}\n\n')
        file.write(f'## Answer:\n{answer}\n\n')

# Main program loop
while True:
    prompt, answer = generate_prompt()
    write_to_markdown(prompt, answer)

    # Wait for 3 minutes
    time.sleep(180)
