## Overview
Analyzing sentiments related to various products such as Tablet, Mobile and various other gizmos can be fun and difficult especially when collected across various demographics around the world. In this weekend hackathon, we challenge the machinehackers community to develop a machine learning model to accurately classify various products into 4 different classes of sentiments based on the raw text review provided by the user. Analyzing these sentiments will not only help us serve the customers better but can also reveal lot of customer traits present/hidden in the reviews.

The sentiment analysis requires a lot to be taken into account mainly due to the preprocessing involved to represent raw text and make them machine-understandable. Usually, we stem and lemmatize the raw information and then represent it using TF-IDF, Word Embeddings, etc. However, provided the state-of-the-art NLP models such as Transformer based BERT models one can skip the manual feature engineering like TF-IDF and Count Vectorizers.

In this short span of time, we would encourage you to leverage the ImageNet moment (Transfer Learning) in NLP using various pre-trained models.

 

## Dataset Description:

Train.csv - 6364 rows x 4 columns (Inlcudes Sentiment Columns as Target)
Test.csv - 2728 rows x 3 columns
Sample Submission.csv - Please check the Evaluation section for more details on how to generate a valid submission
 

## Attribute Description:

Text_ID - Unique Identifier
Product_Description - Description of the product review by a user
Product_Type - Different types of product (9 unique products)
Class - Represents various sentiments
0 - Cannot Say
1 - Negative
2 - Positive
3 - No Sentiment

## Skills:
NLP, Sentiment Analysis
Feature extraction from raw text using TF-IDF, CountVectorizer
Using Word Embedding to represent words as vectors
Using Pretrained models like Transformers, BERT
Optimizing multi-class log loss to generalize well on unseen data

## LeaderBoard:
### Private LB: 8th rank
### Public LB: 7th rank
[https://www.machinehack.com/hackathons/product_sentiment_classification_weekend_hackathon_19]
