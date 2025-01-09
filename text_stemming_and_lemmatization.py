import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer, WordNetLemmatizer
from nltk.corpus import wordnet

# Sample text (replace this with actual text)
text = """
Wake up to reality! Nothing ever goes as planned in this accursed world. The longer you live, the more you realize that the only things that truly exist in this reality are merely pain. suffering and futility.
"""

# Tokenize the text
tokens = word_tokenize(text)

# Initialize stemmers and lemmatizer
ps, ls, ss = PorterStemmer(), LancasterStemmer(), SnowballStemmer('english')
lemmatizer = WordNetLemmatizer()

# Lemmatization and Stemming results
result = {
    "PorterStemmer": [ps.stem(word) for word in tokens],
    "LancasterStemmer": [ls.stem(word) for word in tokens],
    "SnowballStemmer": [ss.stem(word) for word in tokens],
    "WordNetLemmatizer": [lemmatizer.lemmatize(word.lower(), wordnet.VERB) for word in tokens]
}

# Output the results
print(result)
