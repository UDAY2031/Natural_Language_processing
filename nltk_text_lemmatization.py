import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize
from nltk import pos_tag

# Input text
text = """
Wake up to reality! Nothing ever goes as planned in this accursed world. The longer you live, the more you realize that the only things that truly exist in this reality are merely pain. suffering and futility. Listen, everywhere you look in this world, wherever there is light, there will always be shadows to be found as well. As long as there is a concept of victors, the vanquished will also exist. The selfish intent of wanting to preserve peace, initiates war. and hatred is born in order to protect love. There are nexuses causal relationships that cannot be separated.
"""

# Function to map POS tag to WordNet POS tag
def a(tag):
    return {'J': wordnet.ADJ, 'V': wordnet.VERB, 'N': wordnet.NOUN, 'R': wordnet.ADV}.get(tag[0], wordnet.NOUN)

# Tokenize the text
tokens = word_tokenize(text)

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# POS tagging
pos_tags = pos_tag(tokens)

# Lemmatize words based on their POS tag
lemmatized = [lemmatizer.lemmatize(word, a(tag)) for word, tag in pos_tags]

# Output the lemmatized words
print("Lemmatized Words:")
print(lemmatized)
