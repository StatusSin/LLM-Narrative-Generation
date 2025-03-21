from openai import OpenAI
import finalGame2024.prompt_model as prompt_model
import random as rand
import finalGame2024.api_key as api_key
from excel_output import append_to_excel

class Setup:
    def __init__(self, setting, location, problem):
        self.setting = setting
        self.location = location
        self.problem = problem
        self.client = OpenAI(api_key=api_key.getKey())
        self.model = "gpt-3.5"
        self.history = []

    def interact(self, character, player_input):
        history_context = "While keeping in mind that this is the previous interactions in the conversation; Each player input will be prefaced by the 'player:' signifier, and each response by the character you will be acting as will be prefaced by the 'Blacksmith:' signifier."
        prompt_npc = "Given setting: " + self.setting + " & Given locations" + self.location + " & given" + self.problem + "respond to the adventurer talking to you. This is what they have just said to you:" + player_input + ",and you are this person:" + character + history_context + str(self.history) + "write your response as "+ character + " make sure the response is not lengthy."
        response_text = prompt_model.promptModel(self.client, prompt_npc)
        history = player_input + response_text
        # print("\n\nhistory" + history+ "\n\n")
        self.history.append(history)
        # append_to_excel("gpt_output.xlsx", [prompt_npc] + [response_text])
        return response_text
        
    def record(self,response_text, player_input, player_history):
        record = "Given the" + response_text + "and the player input" + player_input + "and the player history" + player_history + "please evaluate the relelvance of the player input to the overall conversation and plot as either relevant, kind_of_relevant or irrelevant."
        response_text = prompt_model.promptModel(self.client, record)
        append_to_excel("gpt_output.xlsx", [response_text, player_input] + [record])

    def mood_setter(self,response_text):
        moods = ['Happy', 'Sad', 'Angry', 'Excited', 'Anxious', 'Calm', 'Confused', 'Surprised', 'Bored', 'Tired']
        mood_question = "Given " + response_text + "please assign a mood to the character from the following list: " + moods
        response_text = prompt_model.promptModel(self.client, mood_question)
        return response_text
    
game = Setup("Medieval Town", "Marketplace", "There is a dragon going to attack the town")
while True:
    player = "player: " + input("Message to Blacksmith: ")
    character = "Blacksmith"
    response_text = character + ": " + game.interact("Blacksmith", player)
        
    print(response_text)
    game.history.append(response_text + player)
    game.record(response_text, player, str(game.history))