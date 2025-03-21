import finalGame2024.prompt_model as prompt_model
import finalGame2024.api_key as api_key
from openai import OpenAI


def create_environment(self, player_input, character, setting, location, problem):
   client = OpenAI(api_key=api_key.getKey())

   prompt_environment = "Given this environmnet" + player_input + "please describe the environment in detail, and include this character: " + character + "in the setting of" + setting + "and the location of" + location + "with the problem of" + problem

   response_text = prompt_model.promptModel(client, prompt_environment)

   return response_text