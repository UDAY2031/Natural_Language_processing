import nltk
from nltk import word_tokenize, ngrams
from collections import Counter

# Small sample text
text = "Machine learning is amazing."

# Tokenize and create bigrams
tokens = word_tokenize(text.lower())
bigrams = list(ngrams(tokens, 2))

# Count bigrams and words
bigram_counts = Counter(bigrams)
word_counts = Counter(tokens)
vocab_size = len(word_counts)

# Laplace smoothing function
def bigram_prob(bigram):
    return (bigram_counts[bigram] + 1) / (word_counts[bigram[0]] + vocab_size)

# Example bigram probability
print(f"Probability of ('machine', 'learning'): {bigram_prob(('machine', 'learning')):.4f}")
