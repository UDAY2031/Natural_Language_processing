import nltk
from nltk import word_tokenize, ngrams
from collections import Counter

# Sample corpus
corpus = [
    "Technology is rapidly evolving in the modern world.",
    "Advancements in computing are transforming industries.",
    "Artificial intelligence is one of the most exciting fields."
]

# Tokenize and create bigrams
tokens = [word_tokenize(doc.lower()) for doc in corpus]
bigrams = [bigram for doc in tokens for bigram in ngrams(doc, 2)]

# Count bigrams and words
bigram_counts = Counter(bigrams)
word_counts = Counter([word for doc in tokens for word in doc])
vocab_size = len(word_counts)

# Laplace smoothing function
def bigram_prob(bigram):
    return (bigram_counts[bigram] + 1) / (word_counts[bigram[0]] + vocab_size)

# Example bigram probability
print(f"Probability of ('technology', 'is'): {bigram_prob(('technology', 'is')):.4f}")
