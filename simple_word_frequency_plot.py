import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
from nltk.probability import FreqDist
import string

# Input text
text = """
Wake up to reality! Nothing ever goes as planned in this accursed world. The longer you live, the more you realize that the only things that truly exist in this reality are merely pain. suffering and futility. Listen, everywhere you look in this world, wherever there is light, there will always be shadows to be found as well.
"""

# Tokenize, remove stopwords and punctuation
nltk.download('punkt')
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
tokens = [word.lower() for word in word_tokenize(text) if word.isalpha() and word.lower() not in stop_words]

# Frequency distribution and plotting
fdist = FreqDist(tokens)
fdist.plot(10, title="Top 10 Most Frequent Words")
plt.show()
