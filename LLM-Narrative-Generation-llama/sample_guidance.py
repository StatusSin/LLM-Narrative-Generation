import guidance
from guidance import models, gen

llama = models.LlamaCpp('orca_mini_v3_7b.Q4_K_M.gguf', echo=False)


@guidance
def qa_bot(lm, query):
    lm += f'''\
    Q: {query}
    A: {gen(name="answer", stop="Q:")}'''
    return lm


query = "Describe a unique jungle enviornment"
lm = llama + qa_bot(query)

print(lm)