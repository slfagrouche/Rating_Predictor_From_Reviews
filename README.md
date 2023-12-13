# Amazon-Team-Fall-DS-Project-

Model to predict the product rating base on product review: Amazon rating machine 

Data Set: https://www.kaggle.com/datasets/cynthiarempel/amazon-us-customer-reviews-dataset?datasetId=1412891

Team:
Rahat Fahim,
Kazi,
Said




# Predicting Amazon Product Ratings from Review Comments

## Summary

### Project Purpose:
The objective of this project was to develop a model capable of predicting a user's star rating (on a scale of 1–5) for various Amazon products based on the textual content of their review comments. The focus was not limited to a specific product category but aimed to provide a versatile solution applicable to diverse items. The project involved testing several Neural Network algorithms, leveraging Natural Language Processing (NLP) techniques for text tokenization and vectorization.

### Data and Code Used:
The dataset comprised approximately over 54GB open-source from Kaggle Amazon user reviews. Due to processing limitations, the analysis was performed on a 10% random sample of the dataset. The entire codebase is available in the provided Jupyter notebook.

### Methodology Overview:
The project involved exploring six different algorithm and NLP vectorization combinations, including Support Vector Machine (SVM), Deep Neural Network (DNN), and Convolutional Neural Network (CNN) models. Text data underwent sampling, tokenization, normalization, and vectorization before being partitioned into training and testing sets.

## Text Data Pre-Processing

### Sampling the Dataset:
To address the dataset's size, a 10,000-record sample was utilized, with weighted probability for records with < 5 stars to counteract rating skewness.

### Tokenization:
Text data underwent tokenization, extracting distinct features for each word while excluding common stopwords.

### Normalization:
Normalization involved removing non-ASCII characters, punctuation, converting to lowercase, and replacing numbers with textual representation. Lemmatization was applied to normalize verb forms.

### Vectorization:
Vectorization transformed text data into numeric matrices using Bag of Words (BOW).

## Modeling

### Deep Neural Network (DNN):
A DNN was implemented using BOW and trained word embedding vectorization techniques. The model included hidden layers, an Adam optimizer, categorical cross-entropy loss function, and softmax activation. DNNs exhibited high training accuracy (92–95%) with modest overall accuracy (~90%).

## Conclusion
The project provided valuable insights into Neural Net architectures, NLP techniques, and challenges in predicting user ratings from review comments. Further exploration could address overfitting concerns, imbalanced datasets, and incorporate additional features for improved predictive accuracy. The versatility of the developed models allows adaptation to diverse Amazon product categories.


