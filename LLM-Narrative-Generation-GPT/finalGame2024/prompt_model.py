from openai import OpenAI

def promptModel(client, prompt):
    response = client.chat.completions.create(
        model="gpt-4",
        # response_format = {"type": "json_object"},
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content