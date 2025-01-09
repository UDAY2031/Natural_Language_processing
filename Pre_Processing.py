import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Download necessary NLTK data files (uncomment these lines if running for the first time)
# nltk.download('punkt')
# nltk.download('stopwords')

# Input text
text = ""

# Tokenization
tokens = word_tokenize(text)

# Removing stopwords
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

# Stemming
stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]

# Joining tokens to create preprocessed text
preprocessed_text = ' '.join(stemmed_tokens)

# Print results
print("Original Text:", text)
print("Tokens:", tokens)
print("Filtered Tokens (without stopwords):", filtered_tokens)
print("Stemmed Tokens:", stemmed_tokens)
print("Preprocessed Text:", preprocessed_text)
