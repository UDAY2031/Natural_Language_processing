import pandas as pd
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('vacination_tweets.csv', encoding='latin1')

# Define a function to classify sentiment
def classify_sentiment(text):
    sentiment_score = TextBlob(str(text)).sentiment.polarity
    if sentiment_score > 0:
        return 'positive'
    elif sentiment_score < 0:
        return 'negative'
    else:
        return 'neutral'

# Apply the sentiment classification function to the 'text' column
data['sentiment_category'] = data['text'].apply(classify_sentiment)

# Generate word clouds
def generate_wordcloud(category, color):
    text = " ".join(data[data['sentiment_category'] == category]['text'].astype(str))
    return WordCloud(width=800, height=400, background_color='white', colormap=color).generate(text)

positive_wordcloud = generate_wordcloud('positive', 'Greens')
negative_wordcloud = generate_wordcloud('negative', 'Reds')
neutral_wordcloud = generate_wordcloud('neutral', 'Blues')

# Plot word clouds
plt.figure(figsize=(18, 6))
plt.subplot(1, 3, 1), plt.imshow(positive_wordcloud), plt.axis('off'), plt.title('Positive Words')
plt.subplot(1, 3, 2), plt.imshow(negative_wordcloud), plt.axis('off'), plt.title('Negative Words')
plt.subplot(1, 3, 3), plt.imshow(neutral_wordcloud), plt.axis('off'), plt.title('Neutral Words')
plt.tight_layout()
plt.show()

# Print sentiment analysis results
print(data[['text', 'sentiment_category']].head(5))  # Adjust number as needed

# Print sentiment category counts
print(data['sentiment_category'].value_counts())
