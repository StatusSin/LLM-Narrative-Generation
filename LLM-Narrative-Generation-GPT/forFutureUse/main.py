import excel_output
from openai import OpenAI
import finalGame2024.prompt_model as prompt_model
from characters import Characters
import forFutureUse.characterMaker as characterMaker
import finalGame2024.api_key as api_key
import forFutureUse.plotMaker as plotMaker

def main():

    char_manager = Characters()

    # Adding a character
    # char_manager.add_character("Matt", 
    #                         "A 21 year old lanky asian man with black shoulder length hair and dark eyes. He has a scar on his elbow from an accident. They dress in baggy clothes and have black earrings.",
    #                         "He is a college student studying computer science. In his spare time he voulenteers to feed the hungry and plays guitar.",
    #                         "holds the key to the treasure, but will only give it to a worth person. He would determine worthiness by the person's intelegence.",
    #                         2,
    #                         "he/they")

    # Accessing a character's description
    print(char_manager.describe_character("Matt"))
    key = api_key.getKey()

    client = OpenAI(api_key=key)
    prompt_base = "You are a character described as Red. Respond to a call for help given that you are this character: "
    user_input = "Help, I'm lost in the forest!"
    model = "gpt-4"

    full_prompt = prompt_base + user_input
    # response_text = prompt_model.promptModel(client, prompt_base, model)

    # # Append the response to the Excel file
    # excel_output.append_to_excel("gpt_output.xlsx", [full_prompt, response_text])

    excel_output.append_to_excel("gpt_output.xlsx", [full_prompt, plotMaker.makePlot()])

if __name__ == "__main__":
    main()