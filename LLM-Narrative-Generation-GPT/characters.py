class Character:
    def __init__(self, name, description, background, relevance, alignment, pronouns):
        self.name = name
        self.description = description
        self.background = background
        self.relevance = relevance
        self.alignment = alignment
        self.pronouns = pronouns

    def describe(self):
        return (f"Name: {self.name}. Description: {self.description}. Background: {self.background}. "
                f"Relevance: {self.relevance}. Alignment: {self.alignment}. Pronouns: {self.pronouns}.")

class Characters:
    def __init__(self):
        self.characters = {}

    def add_character(self, name, description, background, relevance, alignment, pronouns):
        character = Character(name, description, background, relevance, alignment, pronouns)
        self.characters[name] = character

    def get_character(self, name):
        return self.characters.get(name)

    def describe_character(self, name):
        character = self.get_character(name)
        if character:
            return character.describe()
        else:
            return "Character not found."

""" FORNOTES
Iterative charachter building: name -> name & physical description -> etc...
alignment (choose from options)


look up LangChain

Conversation Log method
-> Respond to diologue method (player /talk)?


to excel some diologue outputs from characters

Game Class
    generate enviornment method
"""