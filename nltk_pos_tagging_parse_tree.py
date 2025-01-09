import nltk
from nltk import pos_tag, word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt

# Ensure NLTK resources are downloaded
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Input text
text = "Natural Language Processing is an exciting field of Artificial Intelligence."

# Tokenization
tokens = word_tokenize(text)

# Part-of-speech tagging
pos_tags = pos_tag(tokens)
print("POS Tags:")
print(pos_tags)

# Define grammar and parse tree
grammar = "NP: {<DT>?<JJ>*<NN>}"  # Noun Phrase grammar
chunk_parser = nltk.RegexpParser(grammar)
t = chunk_parser.parse(pos_tags)

# Print the parse tree
print("\nParse Tree:")
t.pretty_print()

# Plot frequency distribution of words
print("\nMost Frequent Words:")
fdist = FreqDist(tokens)
fdist.plot(10, title="Most Frequent Words")
