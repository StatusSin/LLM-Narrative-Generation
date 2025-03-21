from openai import OpenAI

client = OpenAI(api_key='')
import pandas as pd



def query_gpt(prompt, model="gpt-4-1106-preview", max_tokens=100):
    """
    This function sends a prompt to the GPT API and 
    returns the text response.
    """
    try:
        response = client.completions.create(model=model,
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.7)
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    prompts = [
        "What is the capital of France?",
    ]

    results = []

    for prompt in prompts:
        result = query_gpt(prompt)
        if result is not None:
            results.append({"Prompt": prompt, "Answer": result})

   
    df = pd.DataFrame(results)


    df.to_excel("gpt_output.xlsx", index=False)

if __name__ == "__main__":
    main()
