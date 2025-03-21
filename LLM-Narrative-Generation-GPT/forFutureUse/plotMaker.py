from openai import OpenAI
import finalGame2024.prompt_model as prompt_model
import random as rand
import finalGame2024.api_key as api_key
from excel_output import append_to_excel

class Setup:
    def __init__(self, setting, locations):
        self.setting = setting
        self.locations = locations

    def make_plot(self):
        opening = "Given a kingdom as a setting  Make a problem and create a introductory paragraph, no more than 5 sentences, introducing a town fitting of the setting, describe only one point of interest from the locations list"
        quest = "create a quest for a player based on the problem. The solution to said problem should be a completable in one step."
        characters = "Please make a list of characters all with individual objectives and opinions/ plot relevance to the problem. This list should be called 'characters' and should be a list of dictionaries with the format of name, objective, and opinion. Please preface and follow each character name with a *. Please Preface and follow each objective with a - and each opinion with a ~."
        locations = "Please make a list of locations all with individual attributes. This list should be called 'locations' and should be a list of dictionaries with the format of name, attribute, and description. Please preface and follow each location name with a *. Please Preface and follow each attribute with a - and each description with a ~."
        plot_steps = "You are going to be the game master of this game.  Please after this outline the steps the player must take to complete the quest and format it in a list."
        client = OpenAI(api_key=api_key.getKey())
        solution = []
        prompt_opening = "Please seperate these responses into sections with the format heading: heading text, with a new line after the section is done" + "opening" + opening + "quest" + quest + "characters" + characters + "locations" + locations + "plot_steps" + plot_steps
        response_text = prompt_model.promptModel(client, prompt_opening)
        solution.append(response_text)
        # print(response_text)

        # characters = self.parse(characters)
        # print(characters)
        # for character in characters:
        #     print(str(character))

        # for key in prompt_dictionary:
        # the_variable = prompt_dictionary["solution"]

        response_text = prompt_model.promptModel(client, prompt_opening)
        solution.append(response_text)   
        append_to_excel("gpt_output.xlsx", [prompt_opening] + solution)
        return response_text
    
    def isolate_intro():
        client = OpenAI(api_key=api_key.getKey())
        # response_text = prompt_model.promptModel(client, "given this text" + response_to_make_plot + "Please return the introductory paragraph from the text and describe the town and give the player a hint towards the first step to solving the problem")
        intro = "In the kingdom of Keck, the town of Kettle is a bustling hub of activity. The smell of fresh bread wafts through the air as merchants hawk their wares in the market square. Unfortunatly, the princess Natasha has fallen ill and the only known cure is missing. Whispers of a mysterious herb that grows in the nearby forest have begun to circulate, and the townspeople are looking for a brave adventurer to retrieve it. Will you be the one to save the princess?"
        # return response_text
        return intro
    
    def isolate_character():
        client = OpenAI(api_key=api_key.getKey())
        # response_text = prompt_model.promptModel(client, "Given this text" + response_to_make_plot + "Please isolate the characters and their attributes from the text")
        characters = {"Natasha": "is the ill princess of the kindom. She is in need of the cure to her illness. She is loved by all of the townspeople. She is in a coma and needs the cure quickly.", 
                      "Henry": "is the inkeeper and the barkeep of the local tavern. He is a jovial man. He is in need of a new shipment of ale. He is a good friend of the blacksmith. He will give the player a free room and information on where the herb is if they bring him the ale. He knows that the herb is in the forest by the river, and that the river is guarded by a troll. He will send the player to the blacksmith for a weapon to defeat the troll.",
                      "The blacksmith": "is a burly man with a heart of gold. He is in need of a new shipment of iron. He is a good friend of the innkeeper. He will give the player a weapon to defeat the troll if they bring him the iron. He knows very little about the herb, but will send the player to the innkeeper for information on where it is. He will also tell the player to go to the inkeeper if they have not already gone there.",
                      "The troll": "is a large, ugly creature that guards the herb by the river. He will try to attack the player if they go near the herb. To defeat him, the player will need a weapon from the blacksmith. Once the troll is defeated, the player can retrieve the herb and return it to the princess."
        }
        return characters
 
    
    def isolate_location():
        # client = OpenAI(api_key=api_key.getKey())
        # response_text = prompt_model.promptModel(client, "Given this text" + response_to_make_plot + "Please isolate the location and their attributes from the text")
        return ["town","blacksmith", "tavern", "forest", "river", "inn", "castle"]
    
    def isolate_quest():
        # client = OpenAI(api_key=api_key.getKey())
        # response_text = prompt_model.promptModel(client, "Given this text" + response_to_make_plot + "Please isolate the quest from the text")
        return "Save the princess from her illness"
    

    #if more than 1 of each, will overwrite - need to change
    #maybe prefix each location/character, and recurse parse for each instance
    def parse(self, parse_text):
        fields = {'*': 'name', '-': 'objective', '~': 'opinion'}
        results = {'name': None, 'objective': None, 'opinion': None}
        active_field = None

        index = 0
        while index < len(parse_text):
            char = parse_text[index]
            if char in fields:
                if active_field:
                    active_field = None  
                else:
                    active_field = fields[char] 
                    if index + 1 < len(parse_text): 
                        results[active_field] = parse_text[index + 1] 
                    index += 1
            index += 1

        return results

    
# game = Setup("Medieval Town", "Tavern, Market, Castle, Blacksmith, Inn, Alley")