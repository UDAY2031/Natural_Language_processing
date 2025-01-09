from nltk import word_tokenize, ngrams

# Input text
text = """
Wake up to reality! Nothing ever goes as planned in this accursed world. The longer you live, the more you realize that the only things that truly exist in this reality are merely pain. suffering and futility. Listen, everywhere you look in this world, wherever there is light, there will always be shadows to be found as well. As long as there is a concept of victors, the vanquished will also exist. The selfish intent of wanting to preserve peace, initiates war. and hatred is born in order to protect love. There are nexuses causal relationships that cannot be separated.

I want to severe the fate of this world. A world of only Victors. A world of only Peace. A world of only love. I will create such a world.

I am.

The Ghost Of The Uchiha
"""

# Tokenize the text
tokens = word_tokenize(text)

# Generate trigrams
trigrams = list(ngrams(tokens, 3))

# Output the trigrams
print("Trigrams:")
for trigram in trigrams:
    print(trigram)
