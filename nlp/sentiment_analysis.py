import spacy
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob

class SentimentAnalyzer:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        self.nlp = spacy.load("en_core_web_sm")

    def preprocess_lyrics(self, lyrics):
        tokens = word_tokenize(lyrics)

        filtered_tokens = [word for word in tokens if word.lower() not in self.stop_words]

        lemmatized_tokens = [self.lemmatizer.lemmatize(word) for word in filtered_tokens]

        return ' '.join(lemmatized_tokens)

    def analyze_sentiment(self, lyrics):
        preprocessed_lyrics = self.preprocess_lyrics(lyrics)

        blob = TextBlob(preprocessed_lyrics)
        sentiment_score = blob.sentiment.polarity

        if sentiment_score > 0:
            sentiment_label = "Positive"
        elif sentiment_score < 0:
            sentiment_label = "Negative"
        else:
            sentiment_label = "Neutral"

        return {
            "score": sentiment_score,
            "label": sentiment_label
        }

# Example usage:
if __name__ == "__main__":
    analyzer = SentimentAnalyzer()
    lyrics = "Your sample lyrics here."
    sentiment_result = analyzer.analyze_sentiment(lyrics)
    print(sentiment_result)

