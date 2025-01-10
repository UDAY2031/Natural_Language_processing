import nltk
from textblob import TextBlob

text = """Wake up to reality! Nothing ever goes as planned in this accursed world. The longer you live, the more you realize that the only things that truly exist in this reality are merely pain, suffering, and futility. Listen, everywhere you look in this world, wherever there is light, there will always be shadows to be found as well. As long as there is a concept of victors, the vanquished will also exist. The selfish intent of wanting to preserve peace initiates war, and hatred is born in order to protect love."""
tokens = nltk.pos_tag(nltk.word_tokenize(text))
nouns = [word for word, tag in tokens if tag.startswith('NN')]
adjectives = [word for word, tag in tokens if tag.startswith('JJ')]

print(f'Nouns: {nouns}')
print(f'Adjectives: {adjectives}')
print(f'Sentiment: {TextBlob(" ".join(adjectives)).sentiment}')
