import openai

def generate_text(prompt):
    openai.api_key = "API KEY"
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",  # Updated engine
        prompt=prompt,
        max_tokens=100,  # Adjust max tokens as needed
        n=1,  # Number of completions to generate
        stop=None,  # Stop generating after encountering a stop sequence
    )

    return response.choices[0].text.strip()

