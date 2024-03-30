from openai import OpenAI

def promptModel(client, prompt, model):
    response = client.chat.completions.create(
        model=model,
        # response_format = {"type": "json_object"},
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content