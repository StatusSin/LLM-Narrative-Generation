import random
import forFutureUse.plotMaker as plotMaker
# import npc_interaction
import forFutureUse.characterMaker as characterMaker
import random

class Location:
    def __init__(self, name, attribute, description):
        self.name = name
        self.attribute = attribute
        self.description = description

class Character:
    def __init__(self, name, objective, opinion):
        self.name = name
        self.objective = objective
        self.opinion = opinion

class Game:
    def __init__(self):
        self.problems = [
            "There is a dragon terrorizing the kingdom and the knights have been unable to defeat it.",
            "The princess of the kingdom is sick and the only known cure is missing",
            "The local blacksmith needs to figure out how to make bronze but does not know what to combine"
        ]
        self.locations = [
            Location("Medieval Town", "town", "The town is bustling with people and the smell of food fills the air."),
            Location("Dragon's Lair", "cave", "The cave is dark and damp with the sound of a dragon's roar echoing through the walls."),
            Location("Forest", "forest", "The forest is dense with trees and the sound of birds chirping fills the air.")
        ]
        self.current_location = self.locations[0]
        self.play = False
        self.conversation = False
        self.quest = None
        self.characters = [
            Character("Blacksmith", "Make weapons", "Happy")
        ]
        self.history = []

    def start_phase(self):
        print("Welcome to the game! You will be given a prompt and you have to complete the story.")
        # print("Here are your commands:" +  keywords)
        start = input("Type 'play' to start the game: ")
        if start.lower() == "play":
            print("")
            self.play = True
            # print(random.choice(self.problems))
            response = plotMaker.Setup.make_plot(self)
            print(plotMaker.Setup.isolate_intro(response))

            # self.quest = plotMaker.Setup.isolate_quest(response)

            # locations = plotMaker.Setup.parse(self,plotMaker.Setup.isolate_location(response))
            # #parse is hard-coded to parsing characters, need to change to dynamically return
            # newLocation = Location(locations["name"], locations["objective"], locations["opinion"])
            # self.locations.append(newLocation)

            # characters = plotMaker.Setup.parse(self,plotMaker.Setup.isolate_character(response))
            # newCharacter = Character(characters["name"], characters["objective"], characters["opinion"])
            # self.characters.append(newCharacter)
                        
        elif start.lower() == "quit":
            self.quit_game()
        else:
            print("Invalid input. Please type 'play' to start the game or 'quit' to exit the game.")
            print("")
            self.start_phase()
        if self.play:
            self.action_phase()
    
    def action_phase(self):
        player_input = input("\nWhat would you like to do next?\n")
        if  player_input.lower() == "quit":
            self.quit_game()

        elif player_input.lower() == "help":
            self.help()
            self.action_phase()

        elif player_input.lower() == "talk":
            self.conversation = True
            print("\nWho would you like to talk to?\n")
            if self.current_location.name == "river":
                print("Troll")
            elif self.current_location.name == "tavern":
                print("Inkeeper Henry")
            elif self.current_location.name == "blacksmith":
                print("Blacksmith")
            else:
                print("There are no characters in this location, please type 'travel' to go to a different location.")
                self.conversation = False

                
            person = input("\nType the name of the person you would like to talk to: ")

            if person.lower() == "quit":
                self.quit_game()
                self.conversation = False
            elif person.lower() in self.characters:
                # setUp = npc_interaction.Setup("Medieval Town", self.current_location.name, self.quest)
                # self.talking_phase(setUp, person)
                pass
            else:
                print([character.name for character in self.characters])
                self.action_phase()
                
        elif player_input.lower() == "travel":
            self.traveling_phase()
            
        else:
            print("\nInvalid input. Please type 'help' to see the available commands.\n")
            self.action_phase()
             
    def talking_phase(self, npc, person):
        talk = input("\nWhat would you like to say to " + person + "?")
        if talk.lower() == "leave":
            self.conversation = False
            self.action_phase()
        elif talk.lower() == "help":
            print("\nHere are your commands:\n")
            print("- leave: type in just 'leave' and you will be given taken out of talking")
        
        response = npc.interact(person, talk)
        print(response)
        
        self.history.append(talk, response)

        if self.conversation:
            self.talking_phase(npc,person)

    def traveling_phase(self):
        locations = []
        print("\nWhere would you like to travel to?\n")
        for location in self.locations:
            locations.append(location.name)
            print(location.name)
        newLocation = input().lower()

        if newLocation.lower == "help":
            print("\nHere are your commands:\n")
            print("- cancel: type in just 'cancel' and you will be taken out of travel")

        elif newLocation.lower == 'cancel':
            print("\nLeaving travel.\n")
            self.action_phase()  

        elif newLocation in locations:
            self.current_location = newLocation
            print("\nYou have traveled to the " + newLocation + ".")
            
        else:
            print("\nThat is not a valid location\n")
            self.traveling_phase()

    def help(self):
        print("\nHere are your commands:\n")
        print("- talk: type in just 'talk' and you will be given talk options")
        print("- travel: type in just 'travel' and you will be given travel options")
        print("- quit: type in just 'quit' and the game session will end\n")

    def quit_game(self):
        print("\nQuitting the game.\n")
        self.play = False

game = Game()
game.start_phase()


#We need to utilize the generation of plotmaker to define all available locations and characters
#Need to organize and error handle talk phase
