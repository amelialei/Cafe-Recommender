# Cafe-Recommender

## Overview
This project builds a personalized cafe recommendation system using Yelp's academic dataset, which includes business and review data. The system applies collaborative filtering, sentiment analysis, and location-based filtering to provide cafe recommendations tailored to users' preferences. The system focuses on cafes and tea businesses, combining user similarity, sentiment analysis from reviews, cafe proximity, and business features like free WiFi.

## Features
Collaborative Filtering: Recommends cafes based on users with similar preferences.
Sentiment Analysis: Utilizes Natural Language Processing (NLP) to analyze the sentiment of user reviews.
Location-Based Filtering: Prioritizes cafes closer to the user’s current location.
Hybrid Filtering: Combines user similarity, sentiment, and location data to generate highly personalized recommendations.

## Data Sources
The dataset used comes from the Yelp Academic Dataset, which contains detailed business and review information:

Business Dataset: Contains data on various businesses with the columns business_id, name, address, city, state, postal code, latitude, longitude, stars, review_count, is_open, attributes, categories, and hours.
Review Dataset: Contains data on the reviews for each business with the columns review_id, user_id, business_id, stars, date, text, useful, funny, and cool.

