import openai

# Initialize the GPT model
openai.api_key = 'your_openai_api_key'

def generate_code(prompt):
    response = openai.Completion.create(
        engine="text-davinci-004",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    prompt = "Write a Python function that reverses a string."
    print(generate_code(prompt))
