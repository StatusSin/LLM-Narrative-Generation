from openai import OpenAI
import prompt_model
import api_key

plot = ("In the kingdom of Keck, the town of Kettle is a bustling hub of activity. The smell of fresh bread wafts through the air as merchants hawk their wares in the market square. Unfortunately, the princess Natasha has fallen ill and the only known cure is missing. Whispers of a mysterious herb that grows in the nearby forest have begun to circulate, and the townspeople are looking for a brave adventurer to retrieve it. \nWill you be the one to save the princess?")

def score(player_input, plot):
    client = OpenAI(api_key=api_key.getKey())
    player_response_states = [
        "Exactly on track towards the plot",
        "On track towards the plot",
        "Very off track towards the plot",
        "Completely off track towards the plot"
    ]

    player_text_stripper = """Read 'player_text'; 
                exclude articles, connectives, prepositions and quantifiers; 
                include nouns, verbs, and adjectives
                
                return all words left; 
                format the words as such; 
                '- word1' 
                '- word2'
                '- word3'
                DO NOT RETURN CODE BLOCKS
                """

    plot_text_stripper = """Read 'plot_text'; 
                exclude articles, connectives, prepositions and quantifiers; 
                include nouns, verbs, and adjectives
                
                return all words left; 
                format the words as such; 
                '- word1' 
                '- word2'
                '- word3'
                DO NOT RETURN CODE BLOCKS
                """
    
    player_plot_comparer = """"Read 'stripped_player_text' and 'stripped_plot_text';
                return all words that are in both;
                If there are no words in common, return the word NOTHING
                Else format the words as such; 
                '- word1' 
                '- word2'
                '- word3'
                DO NOT RETURN CODE BLOCKS
    """

    prompt_layers = ["""Read 'compare_text'
                      return 'NO' if the word 'NOTHING' appears in 'compare_text'
                                   else return 'YES'
                     DO NOT RETURN CODE BLOCKS""",
                      """Read 'compare_text' 
                      return 'YES' if any NOUNS, VERBS, ADJECTIVES left in 'compare_text'
                                   else return 'NO'
                    DO NOT RETURN CODE BLOCKS""", 
                      """Read 'compare_text'
                      return 'YES' if there are any PROPER NOUNS in 'compare_text'
                                   else return 'NO'
                    DO NOT RETURN CODE BLOCKS""", 
                      """Read 'compare_text'
                      return 'YES' if the words princess, natasha, mysterious, or herb are in 'compare_text'
                                   else return 'NO'
                    DO NOT RETURN CODE BLOCKS"""
    ]

    stripped_player_text = prompt_model.promptModel(client, f"Given this player_text:'{player_input}' {player_text_stripper}")
    stripped_plot_text = prompt_model.promptModel(client, f"Given this plot_text:'{plot}' {plot_text_stripper}")
    compare_text = prompt_model.promptModel(client, f"Given this stripped_player_text:'{stripped_player_text}' and this stripped_plot_text:'{stripped_plot_text}' {player_plot_comparer}")

    # IT DOES NOT HANDLE PLURAL ANYTHING; LOOKING FOR EXACT MATCHES

    assignScore(compare_text, plot, 0, prompt_layers, player_response_states, client)
    

def assignScore(compare_text, plot, depth, prompt_layers, player_response_states, client):
    if depth == 4:
        # print(player_response_states[0])

        return player_response_states[0]
    
    final_evaluation = prompt_model.promptModel(client, f"Given this compare_text:'{compare_text}' {prompt_layers[depth]} DO NOT RETURN CODE BLOCKS")
    # print(final_evaluation)

    if final_evaluation == "YES" or final_evaluation == "'YES'":
        assignScore(compare_text, plot, depth + 1, prompt_layers, player_response_states, client)
    else:
        # print(player_response_states[3 - depth])
        
        return player_response_states[3 - depth]

# Example usage:
# for i in range(1):
#     score("I want to pick flowers", plot)
#     score("I want to head to the Kettle market", plot)
#     score("I want to talk to the merchant in the town square", plot)
#     score("I want to give the princess Natasha the mysterious herb", plot)