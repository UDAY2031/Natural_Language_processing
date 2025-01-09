import spacy

# Load the English model
nlp = spacy.load("en_core_web_sm")

# New sample text
text = "Wake up to reality"

# Process the text
doc = nlp(text)

# Print token dependency and head
for token in doc:
    print(f"{token.text}: {token.dep_} -> {token.head.text}")
