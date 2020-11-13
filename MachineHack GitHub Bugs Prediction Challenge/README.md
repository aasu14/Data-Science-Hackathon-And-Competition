## Overview
Foreseeing bugs, features, and questions on GitHub can be fun, especially when one is provided with a colossal dataset containing the GitHub issues. In this hackathon, we are challenging the MachineHack community to come up with an algorithm that can predict the bugs, features, and questions based on GitHub titles and the text body. With text data, there can be a lot of challenges especially when the dataset is big.  Analyzing such a dataset requires a lot to be taken into account mainly due to the preprocessing involved to represent raw text and make them machine-understandable. Usually, we stem and lemmatize the raw information and then represent it using TF-IDF, Word Embeddings, etc. 

However, provided the state-of-the-art NLP models such as Transformer based BERT models one can skip the manual feature engineering like TF-IDF and Count Vectorizers. In this short span of time, we would encourage you to leverage the ImageNet moment (Transfer Learning) in NLP using various pre-trained models.

In this hackathon, we also have an interesting learning curve for all the machine learning specialists to write some quality code to win the prizes, as the evaluation involves getting a code quality score using the Embold Code Analysis platform here.  

Every participant has to register on the Embold's platform for free as a mandatory step before proceeding with the hackathon.

## Dataset Description:
Train.json - 150000 rows x 3 columns (Includes label Column as Target variable)
Test.json - 30000 rows x 2 columns
Train_extra.json - 300000 rows x 3 columns (Includes label Column as Target variable)
Provided solely for training purposes, can be appended in the train.json for training the model
Sample Submission.csv - Please check the Evaluation section for more details on how to generate a valid submission

## Attribute Description:
Title - the title of the GitHub bug, feature, question
Body - the body of the GitHub bug, feature, question
Label - Represents various classes of Labels
Bug - 0
Feature - 1
Question - 2
Skills:
Natural Language Processing
Feature extraction from raw text using TF-IDF, CountVectorizer
Using Word Embedding to represent words as vectors
Using Pretrained models like Transformers, BERT
Optimizing accuracy score as a metric to generalize well on unseen data
 
## About Embold.io
Write Cleaner Code, Faster.
Embold is a general-purpose static code analyzer that helps developers analyze and improve their code by surfacing issues across four dimensions, including design and duplication. Uncover hard-to-detect anti-patterns that can make your code unmaintainable and lead to error-prone solutions. Save time and effort with Embold’s refactoring support and debug before deployment.

## LeaderBoard:
### 30th Rank
[https://www.machinehack.com/hackathons/predict_github_issues_embold_sponsored_hackathon/leaderboard]
