from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-4.1",
    input="Write a one-sentence bedtime story about a unicorn."
)

# Perfectly worked
print(response.output_text)
# Output
"""
Under the silvery glow of the moon, a gentle unicorn named Starwish tiptoed through a field of glowing flowers, leaving a trail of twinkling dreams for sleepy children everywhere.
"""
