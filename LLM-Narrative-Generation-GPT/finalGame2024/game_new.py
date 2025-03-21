import npc_interact_new
class Game:
    """A simple text-based adventure game where a player must find a cure for an ill princess."""
    
    def __init__(self):
        """Initialize the game with default settings."""
        self.locations = ["town", "blacksmith", "tavern", "forest", "river", "castle"]
        self.current_location = "town"
        self.play = False
        self.conversation = False
        self.quest = "Save the princess from her illness"

        self.blacksmith = (False,"\nIn the bustling heart of the village you find the blacksmith's forge, where a burly man, with soot-blackened hands and a ready smile, pounds iron into shape against the steady rhythm of his hammer.")
        self.tavern = (False,"\nAs you approach the Tavern, you see a warm, welcoming place filled with the laughter of patrons and the rich aroma of hearty meals. Henry, a charming half-elf with a quick wit, stands at the bar, serving ale and stories with equal enthusiasm.")
        self.forest = (False, "\nYou see an ancient forest whispering with secrets in the rustling of its leaves, a canopy of green that stretches endlessly. It's a tranquil, untouched place where sunlight dapples the mossy floor. I would be difficult to find anything in here without knowing what you are looking for.")
        self.river = (False, "\nA wide, gurgling river cuts through the landscape, its waters dark and swirling. Beneath a rickety wooden bridge, a troll guards the river, its eyes gleaming with malice. You can see a herb growing on the other side of the river.")
        self.castle = (False, "\nHigh atop a windswept hill stands a majestic castle, its towers piercing the sky. Within its cold, stone walls, Princess Natasha lies in a canopy bed, her pale face a stark contrast to the vibrant tapestries that adorn her room.")
        self.history = []
        self.knows_about_river = npc_interact_new.test.knows_about_the_river
        self.knows_about_the_blacksmith = npc_interact_new.test.knows_about_the_blacksmith
        self.has_cure = npc_interact_new.test.has_cure
        self.has_sword = npc_interact_new.test.has_sword
        self.intro = ("In the kingdom of Keck, the town of Kettle is a bustling hub of activity. The smell of fresh bread wafts through the air as merchants hawk their wares in the market square. Unfortunatly, the princess Natasha has fallen ill and the only known cure is missing. Whispers of a mysterious herb that grows in the nearby forest have begun to circulate, and the townspeople are looking for a brave adventurer to retrieve it. \nWill you be the one to save the princess?")

    def start_phase(self):
        """Begin the game by introducing the setting and starting the interaction loop."""
        print("Welcome to the game! You will be given a prompt and you have to complete the story.")
        while not self.play:
            start = input("Type 'play' to start the game: ").lower()
            if start == "play":
                self.play = True
                print("\n" + self.intro)
                self.action_phase()
            elif start == "quit":
                self.quit_game()
            else:
                print("Invalid input. Please type 'play' to start the game or 'quit' to exit the game.\n")
    
    def action_phase(self):
        """Handle player inputs for actions within the game."""
        while self.play:
            player_input = input("\nWhat would you like to do? Type 'help' for options: ").lower()
            if player_input == "quit":
                self.quit_game()
            elif player_input == "help":
                self.help()
            elif player_input == "talk":
                self.talking_phase()
            elif player_input == "travel":
                self.traveling_phase()
            elif player_input == "location":
                print("\nYou are currently in " + self.current_location + ".")
            else:
                print("\nInvalid input. Please type 'help' to see the available commands.\n")

    def talking_phase(self):
        """Manage conversations between the player and NPCs based on location."""
        print("\nWho would you like to talk to?\n")
        if self.current_location == "river":
            available_characters = ["troll"]
            print("Troll")
        elif self.current_location == "tavern":
            available_characters = ["henry"]
            print("Henry")
        elif self.current_location == "blacksmith":
            available_characters = ["blacksmith"]
            print("Blacksmith")
        elif self.current_location == "castle":
            available_characters = ["natasha"]
            print("Natasha")
        else:
            print("There are no characters in this location, please type 'travel' to go to a different location.")
            return
        
        person = input("\nType the name of the person you would like to talk to: ").lower()
        print(available_characters)
        if person in available_characters:
            self.npc_interact(person)
        else:
            print("There is no one by that name to talk to in this location.")
    
    def traveling_phase(self):
        """Handle location changes for the player within the game world."""
        print("\nWhere would you like to travel to?")
        self.knows_about_river = npc_interact_new.test.knows_about_the_river
        self.knows_about_the_blacksmith = npc_interact_new.test.knows_about_the_blacksmith
        self.has_sword = npc_interact_new.test.has_sword
        self.has_cure = npc_interact_new.test.has_cure

        print(self.locations)
        new_location = input("Type the name of the location you would like to travel to: ").lower()
        if new_location == self.current_location:
            print("\nYou are already in " + new_location + ".")
        elif new_location == "quit":
            self.quit_game()
        elif new_location == "help":
            self.help()
        elif new_location == "location":
            print("\nYou are currently in " + self.current_location + ".")
        elif new_location == "castle" and self.has_cure == False:
            print("\nYou need to find the cure before you can enter the castle.")
        elif new_location == "river" and self.knows_about_river == False:
            print("\nYou do not know where this is yet.")
        elif new_location in self.locations:
            self.current_location = new_location
            print("\nYou have traveled to " + new_location + ".")
            if new_location == self.locations[1] and self.blacksmith[0] == False:
                self.blacksmith = (True, self.blacksmith[1])
                print(self.blacksmith[1])
            elif new_location == self.locations[2] and self.tavern[0] == False:
                self.tavern = (True, self.tavern[1])
                print(self.tavern[1])
            elif new_location == self.locations[3] and self.forest[0] == False:
                self.forest = (True, self.forest[1])
                print(self.forest[1])
            elif new_location == self.locations[4] and self.river[0] == False:
                self.river = (True, self.river[1])
                print(self.river[1])
            elif new_location == self.locations[5] and self.castle == False:
                self.castle = (True, self.castle[1])
                print(self.castle[1])
        else:
            print("\nThat is not a valid location\n")

    def npc_interact(self, character):
        """Simulate interaction with a non-player character."""
        npc_interact_new.test.talk_to_npc(character, self.intro)

    def help(self):
        """Display available commands to the player."""
        print("\nHere are your commands:")
        print("- talk: initiate conversation with a character")
        print("- travel: move to a different location")
        print("- quit: exit the game")
        print("- help: display this help message")
        print("- location: display current location")
        print("- end: end the conversation" "\n")
        if self.current_location == "castle" and self.has_cure == True:
            print("type 'give cure' to give the cure to the princess")
    def quit_game(self):
        """End the game session."""
        self.play = False
        
        
while True:
    game = Game()
    game.start_phase()
    
       
