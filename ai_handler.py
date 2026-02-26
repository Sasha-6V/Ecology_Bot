from openai import OpenAI
from config import OPENROUTER_API_KEY

client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

SYSTEM_PROMPT = """
Ты дружелюбный эксперт по экологии, который посвещает молодежь в неизведанный им мир экологии.
Отвечай креативно, но понятно.
Ты общаешься с детьми, используй эмодзи, но умеренно.
Правила:
- Не используй LaTeX.
- Не используй математическую разметку (\[ \] \( \)).
- Не используй формулы в TeX-стиле.
- Пиши формулы обычным текстом.
"""

def ask_ai(user_text: str):
    # print("USER:", user_text)
    response = client.chat.completions.create(
        model="arcee-ai/trinity-large-preview:free",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_text}
        ],
        temperature=0.8,
        max_tokens=1500
    )

    return response.choices[0].message.content
