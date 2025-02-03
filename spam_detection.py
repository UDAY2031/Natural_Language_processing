import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
import nltk
import re
import matplotlib.pyplot as plt

# Download NLTK resources
nltk.download('stopwords')
nltk.download('wordnet')

from nltk.corpus import stopwords

# Load dataset
data = pd.read_csv('spam.csv', encoding='latin-1')[['v1', 'v2']]
data.columns = ['label', 'message']

# Preprocess text (remove non-alphabetic characters, convert to lowercase, remove stopwords)
stop_words = set(stopwords.words('english'))
data['message'] = data['message'].apply(lambda x: ' '.join(
    word for word in re.sub(r'[^a-zA-Z]', ' ', str(x)).lower().split()
    if word not in stop_words))

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    data['message'], 
    data['label'].apply(lambda x: 'spam' if x == 'spam' else 'not spam'), 
    test_size=0.2, 
    random_state=42
)

# Vectorize text
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train model
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Predict
y_pred = model.predict(X_test_vec)

# Display results
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Plot label distribution
pd.Series(y_pred).value_counts().plot.bar(
    color=['blue', 'orange'], 
    title='Predicted Label Distribution'
)
plt.xlabel('Label')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.show()
