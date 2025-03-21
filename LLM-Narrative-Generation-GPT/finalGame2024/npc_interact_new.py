from openai import OpenAI
import prompt_model as prompt_model
import api_key as api_key
import taskScorer

class ChatWithNPC:
    def __init__(self):
        """
        Initialize the ChatWithNPC class with a client object for API interaction and character information.
        
        Args:
        client (object): Client object responsible for interacting with the AI model.
        character_info (dict): A dictionary containing initial descriptions and states for each character.
        """
        self.client = OpenAI(api_key=api_key.getKey())
        self.natasha_history = ["is the ill princess of the kindom. She is in need of the cure to her illness. She is loved by all of the townspeople. She is in a coma and needs the cure quickly."
        ]
        self.henry_history = ["is the inkeeper and the barkeep of the local tavern. He is a jovial man. He is in need of a new shipment of ale. He is a good friend of the blacksmith. He will give the player a free room and information on where the herb is if they bring him the ale. He knows that the herb is in the forest by the river, and that the river is guarded by a troll. He will send the player to the blacksmith for a weapon to defeat the troll.",
        ]
        self.blacksmith_history = ["is a burly man with a heart of gold. He is in need of a new shipment of iron. He is a good friend of the tavernkeeper. He will give the player a weapon to defeat the troll if they bring him the iron. He knows very little about the herb, but will send the player to the tavernkeeper for information on where it is. He will also tell the player to go to the tavern if they have not already gone there.",
        ]
        self.troll_history = ["is a large, ugly creature that guards the herb by the river. He will try to attack the player if they go near the herb. To defeat him, the player will need a weapon from the blacksmith. Once the troll is defeated, the player can retrieve the herb and return it to the princess"
        ]
        self.knows_about_the_blacksmith = False
        self.knows_about_the_river = False
        self.has_sword = True
        self.has_cure = False
        
    def talk_to_npc(self, character_name, plot):
        """
        Communicate with an NPC using a client object's method to invoke the AI model.

        Args:
        character_name (str): The name of the NPC character.
        player_input (str): The player's input or question to the NPC.

        Returns:
        str: The NPC's response.
        """
        player_input = input("Message to " + character_name + ": ")
        if player_input == "end":
            return "Goodbye!"
        
        if character_name == "natasha":
            character_name = character_name.lower()
            history_text = " ".join(self.natasha_history)
            input_text = "You are the princess Natasha in a video game. in the kingdom of Keck the princess Natasha has fallen ill and the only known cure is missing. You are much too weak to talk to anyone who has not found a cure. Here is your background followed by the conversation history with the player so far" +" ' " + history_text + " ' " + "and this is what has just been said." + " ' " + player_input + " ' " + "What would you like to say to the player? Please keep responses short and answer like a princess would. Without too much extra information."
            response_text = prompt_model.promptModel(self.client, input_text + "Given that the player gave a response" + str(player_input) + "that is" + str(taskScorer.score(player_input, plot)) + ". Respond accordingly based on your knowledge of the plot")
            self.natasha_history.append(f"Player: {player_input}")
            self.natasha_history.append(f"Natasha: {response_text}")
            print(response_text)
            if player_input == "give cure":
                print("You have given the cure to the princess. Congratulations, you have completed the game!")
                print("********\nGoodbye!\n********")
                return "Type quit to play again!"
            return self.talk_to_npc(character_name, plot)
            
        if character_name == "henry":
            character_name = character_name.lower()
            history_text = " ".join(self.henry_history)
            input_text = "You are the local tavern keep in a videogame Please only output your response as the tavern keep and nothing else. The player is passing in their own input so do not worry about that. You work in the kingdom of Keck and the princess Natasha has fallen ill and the only known cure is missing. You have heard Whispers of a mysterious herb that grows in the nearby forest and the townspeople are looking for a brave adventurer to retrieve it. You are talking to the player. You know that your friend the blacksmith has a weapon that will be able to kill the troll guarding the herb, but will not say anything about it unless asked. Here is your background followed by the conversation history with the player so far" + history_text + ",and this is what has just been said." + player_input + ". What would you like to say to the player? Do not help them right away with the quest, wait for them to prompt you to do so. You should tell them about the herb in the forest if they mention the princess, but be secretive and give out information sparingly. Please keep responses short and answer like a tavern keep would. Without too much extra information."
            response_text = prompt_model.promptModel(self.client, input_text + "Given that the player gave a response" + str(player_input) + "that is" + str(taskScorer.score(player_input, plot)) + ". Respond accordingly based on your knowledge of the plot")
            self.henry_history.append(f"Player: {player_input}")
            self.henry_history.append(f"Henry: {response_text}")
            history_text = " ".join(self.henry_history)
            self.progress_story(response_text,character_name)
            print(response_text)
            return self.talk_to_npc(character_name, plot)
            
        if character_name == "blacksmith":
            character_name = character_name.lower()
            history_text = " ".join(self.blacksmith_history)
            if self.knows_about_the_blacksmith == True:
                input_text = "You are the local blacksmith in a videogame. Please only output a response as the blacksmith and nothing else. You work in the kingdom of Keck and the princess Natasha has fallen ill and the only known cure is missing. You mostly keep your head down, so you don't know much of how to help, but you know what your friend Henry who runs the tavern has sent someone over and you should give them a sword that call kill trolls for free if they mention they know him. You are talking to the player. If you give the player a sword, please say it exactly like this 'I hope this sword will help you along your way'. Here is your background followed by the conversation history with the player so far" + history_text + ",and this is what has just been said." + player_input + ". What would you like to say to the player? Do not help them right away with the quest, wait for them to prompt you to do so. Please keep responses short and answer like a blacksmith would. Without too much extra information."
                response_text = prompt_model.promptModel(self.client, input_text + "Given that the player gave a response" + str(player_input) + "that is" + str(taskScorer.score(player_input, plot)) + ". Respond accordingly based on your knowledge of the plot")
                self.blacksmith_history.append(f"Player: {player_input}")
                self.blacksmith_history.append(f"Blacksmith: {response_text}")
                print(response_text)
                self.progress_story(response_text,character_name)
                return self.talk_to_npc(character_name, plot)
            else:
                input_text = "You are the local blacksmith in a videogame. Please only output a response as the blacksmith and nothing else. You work in the kingdom of Keck and the princess Natasha has fallen ill and the only known cure is missing. You mostly keep your head down, so you don't know much of how to help, but you know that your friend Henry, the tavern keep tends to know about these things. You are talking to the player. Try to direct the player to Henry. Here is your background followed by the conversation history with the player so far" + history_text + ",and this is what has just been said." + player_input + ". What would you like to say to the player? Do not help them right away with the quest, wait for them to prompt you to do so. Please keep responses short and answer like a blacksmith would. Without too much extra information."
                response_text = prompt_model.promptModel(self.client, input_text + "Given that the player gave a response" + str(player_input) + "that is" + str(taskScorer.score(player_input, plot)) + ". Respond accordingly based on your knowledge of the plot")
                self.blacksmith_history.append(f"Player: {player_input}")
                self.blacksmith_history.append(f"Blacksmith: {response_text}")
                print(response_text)
                self.progress_story(response_text,character_name)
                return self.talk_to_npc(character_name, plot)
            
        elif character_name == "troll":
            character_name = character_name.lower()
            history_text = " ".join(self.troll_history).lower()
            if self.has_sword == False:
                input_text = "You are the troll in a videogame. Please only output a response as the troll and nothing else. You are guarding the herb by the river in the kingdom of Keck. You are a large, ugly creature that will try to attack the player if they go near the herb. If they mention having a weapon they are lying. You are talking to the player. Here is your background followed by the conversation history with the player so far" + history_text + ",and this is what has just been said." + player_input + ". What would you like to say to the player? Please keep responses short and answer like a troll would. Without too much extra information."
                response_text = prompt_model.promptModel(self.client, input_text + "Given that the player gave a response" + str(player_input) + "that is" + str(taskScorer.score(player_input, plot)) + ". Respond accordingly based on your knowledge of the plot")
                self.troll_history.append(f"Player: {player_input}")
                self.troll_history.append(f"Troll: {response_text}")
                print(response_text)
                return self.talk_to_npc(character_name, plot)
            if self.has_sword == True:
                input_text = "You are the troll in a videogame. Please only output a response as the troll and nothing else. You are guarding the herb by the river in the kingdom of Keck. You are a large, ugly creature that will try to attack the player if they go near the herb. You are talking to the player. If they mention having a weapon you should say the words 'you can take it'. Here is your background followed by the conversation history with the player so far" + history_text + ",and this is what has just been said." + player_input + ". What would you like to say to the player? Please keep responses short and answer like a troll would. Without too much extra information."
                response_text = prompt_model.promptModel(self.client, input_text + "Given that the player gave a response" + str(player_input) + "that is" + str(taskScorer.score(player_input, plot)) + ". Respond accordingly based on your knowledge of the plot")
                self.troll_history.append(f"Player: {player_input}")
                self.troll_history.append(f"Troll: {response_text}")
                print(response_text)
                self.progress_story(response_text,character_name)
                return self.talk_to_npc(character_name, plot)
        else:
            return "I'm sorry, I don't know that character. Please try again."
            
        

    def progress_story(self,history,character_name):
        """
        Progress the story by interacting with different NPCs based on the player's choices.
        """
        if "blacksmith" in history and character_name == "henry":
            print("You have unlocked the blacksmith's location. You can now travel to the blacksmith.")
            self.knows_about_the_blacksmith = True
            
        if "sword" in history and character_name == "blacksmith":
            print("You have received a sword from the blacksmith. You can now travel to the river to face the troll.")
            
        if "river" in history and character_name == "henry":
            print("You have unlocked the river's location. You can now travel to the river.")
            self.knows_about_the_river = True
            
        if "take it" in history and character_name == "troll":
            print("You have defeated the troll and retrieved the herb. You can now travel back to the castle to give the herb to the princess.")
            self.has_cure = True

test = ChatWithNPC()
# test.talk_to_npc("henry")