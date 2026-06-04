from app.core.groq import client
from app.services.prompt_service import build_prompt


def generate_ai_reply(message, state, memory):

    prompt = build_prompt(message, state, memory)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": prompt}
        ]
    )

    return response.choices[0].message.content