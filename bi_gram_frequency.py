from nltk import word_tokenize, ngrams
from collections import Counter

# Sample documents
doc1 = "Technology is rapidly evolving in the modern world. Advancements in computing are transforming industries."
doc2 = "Artificial intelligence is one of the most exciting fields. It has applications in healthcare, finance, and transportation."
doc3 = "Natural language processing is a fascinating field. It enables machines to understand human language."

# Tokenize documents
docs = [doc1, doc2, doc3]
tokens = [word_tokenize(doc.lower()) for doc in docs]

# Generate bi-grams
bi_grams = [bigram for doc in tokens for bigram in ngrams(doc, 2)]

# Count the frequency of bi-grams
bi_gram_freq = Counter(bi_grams)

# Display the top 5 most common bi-grams
top_5_bi_grams = bi_gram_freq.most_common(5)
print(top_5_bi_grams)
