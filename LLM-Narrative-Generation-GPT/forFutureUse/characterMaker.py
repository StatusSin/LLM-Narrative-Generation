from openai import OpenAI
import finalGame2024.prompt_model as prompt_model
import finalGame2024.api_key as api_key

def makeCharacter(self, name = None, pronouns = None, profession = None, description = None, background = None, relevance = None, alignment = None):
    client = OpenAI(api_key=api_key.getKey())
    prompt_dictionary = {"name": "Give me a name for a character.",
                         "pronouns": "What are the character's pronouns?",
                         "profession": "What is the character's profession?",
                         "description": "Describe the character's appearance.",
                         "background": "What is the character's background?",
                         "relevance": "What is the character's relevance to the story?",
                         "alignment": "What is the character's alignment?"
                         }
    
    current_char_info = ""

    for key in prompt_dictionary:
        if key == "name" and name is not None:
            continue
        response_text = prompt_model.promptModel(client, prompt_dictionary[key])
        current_char_info += prompt_dictionary[key]  + ":" + response_text
        makeCharacter(current_char_info)