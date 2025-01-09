import nltk
from nltk import pos_tag, word_tokenize
from nltk.tree import Tree

# Example text and grammar
text = "Wake up to reality. Nothing ever goes as planned in this accursed world."
tokens = word_tokenize(text)
pos_tags = pos_tag(tokens)

grammar = r"""
  NP: {<DT>?<JJ>*<NN>}    # Noun phrase
  PP: {<IN><NP>}          # Prepositional phrase
  VP: {<VB.*><NP|PP>*}    # Verb phrase
"""
chunk_parser = nltk.RegexpParser(grammar)
t = chunk_parser.parse(pos_tags)

# Print tree as text
print("Tree structure:")
print(t.pretty_print())
