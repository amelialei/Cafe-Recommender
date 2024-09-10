import pandas as pd
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from textblob import TextBlob

business_json_path = '/Users/amelialei/yelp_dataset/yelp_academic_dataset_business.json'
bus_df = pd.read_json(business_json_path, lines = True)
bus_df = bus_df[bus_df['is_open'] == 1]
drop_cols = ['is_open', 'review_count']
bus_df = bus_df.drop(drop_cols, axis =1)
bus_df = bus_df[bus_df['categories'].str.contains('Bubble Tea|Coffee and Tea', case = False, na = False)]

review_json_path = '/Users/amelialei/yelp_dataset/yelp_academic_dataset_review.json'
size = 1000000
review = pd.read_json(review_json_path, lines=True, dtype = {'review_id': str, 'user_id': str, 'business_id': str, 'stars': int, 'date': str, 'text': str, 'useful': int, 'funny': int, 'cool': int}, chunksize = size)
chunk_list = []
for review_chunk in review:
    review_chunk = review_chunk.drop(['review_id', 'useful', 'funny', 'cool'], axis=1)
    review_chunk = review_chunk.rename(columns={'stars': 'review_stars'})
    chunk_merged = pd.merge(bus_df, review_chunk, on='business_id', how='inner')
    chunk_list.append(chunk_merged)
df = pd.concat(chunk_list, ignore_index=True, join='outer', axis=0)

df['text'] = (df['text']
              .str.lower()
              .replace(r'\band\b|\bor\b|\bthe\b|\bis\b|\bto\b', '', regex=True)
              .replace(r'[^A-Za-z\s]', '', regex=True))

ps = PorterStemmer()
def tokenize_and_stem(review):
    tokens = word_tokenize(review)
    stemmed_tokens = [ps.stem(token) for token in tokens]
    return ' '.join(stemmed_tokens)

cleaned_reviews = df['text'].apply(tokenize_and_stem)
df['text'] = cleaned_reviews
df['sentiment'] = df['text'].apply(lambda review: TextBlob(review).sentiment.polarity)
