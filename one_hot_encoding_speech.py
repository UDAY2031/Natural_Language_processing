text = """
Wake up to reality! Nothing ever goes as planned in this accursed world. The longer you live, the more you realize that the only things that truly exist in this reality are merely pain, suffering, and futility. Listen, everywhere you look in this world, wherever there is light, there will always be shadows to be found as well. As long as there is a concept of victors, the vanquished will also exist. The selfish intent of wanting to preserve peace, initiates war, and hatred is born in order to protect love. There are nexuses causal relationships that cannot be separated.

I want to sever the fate of this world. A world of only Victors. A world of only Peace. A world of only love. I will create such a world.

I am.

The Ghost Of The Uchiha
"""

# Split the text into words
words = text.split()

# Create a vocabulary and word-to-index mapping
vocab = list(set(words))
word_to_index = {word: idx for idx, word in enumerate(vocab)}

# One-hot encode each word
one_hot_matrix = [[1 if i == word_to_index[word] else 0 for i in range(len(vocab))] for word in words]

# Print results
print("Vocabulary:", vocab)
print("Word-to-index mapping:", word_to_index)
for word, one_hot in zip(words, one_hot_matrix):
    print(f"{word}: {one_hot}")
