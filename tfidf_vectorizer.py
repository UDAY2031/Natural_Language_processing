from sklearn.feature_extraction.text import TfidfVectorizer

# Text for the "Wake up to reality" speech
text = [
    """Wake up to reality! Nothing ever goes as planned in this accursed world. 
    The longer you live, the more you realize that the only things that truly exist in this reality 
    are merely pain, suffering, and futility. Listen, everywhere you look in this world, wherever there is light, 
    there will always be shadows to be found as well. As long as there is a concept of victors, 
    the vanquished will also exist. The selfish intent of wanting to preserve peace, initiates war, 
    and hatred is born in order to protect love. There are nexuses, causal relationships that cannot be separated."""
]

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(text)

# Print the vocabulary and the corresponding TF-IDF matrix
print("Vocabulary:", vectorizer.get_feature_names_out())
print("\nTF-IDF Matrix:\n", tfidf_matrix.toarray())
