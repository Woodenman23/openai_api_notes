from openai import OpenAI

from pathlib import Path

OPEN_AI_API_TOKEN = (Path.home() / ".ssh/openai").read_text().strip()

client = OpenAI(api_key=OPEN_AI_API_TOKEN)

models = ["gpt-4o", "gpt-4o-mini", "gpt-4", "gpt-3.5-turbo"]


def ask_llms(system_role: str, query: str, context: str, previous_query: str) -> None:

    for model in models:
        messages = [
            {
                "role": "system",
                "content": system_role,  # you are a surfer
            },
            {
                "role": "user",
                "content": query,  # user input
            },
            {
                "role": "user",
                "content": context,  # "answer in 30 words or less", "you always end reply with 'and thats the way it goes'"
            },
            {
                "role": "assistant",
                "content": previous_query,
            },
        ]

        completion = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.5,
            max_tokens=1000,
        )

        response = completion.choices[0].message.content

        print(f"{model}: \n\n{response}\n\n######################################")


ask_llms(
    "You are a surfer", "how big is the sun", "always end with 'later man'", "none"
)
