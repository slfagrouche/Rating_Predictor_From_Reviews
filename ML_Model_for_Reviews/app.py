
import streamlit as st   # parameters not required.
from tensorflow.keras.models import load_model
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences

# might need to provide full path to some files for access
tokenizer = None
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

model = load_model('amazon_review.h5')

# st.title ("Amazon Review Neural Network Predictor", '')
# st.header("Please write your review")

product = st.text_input('Product Name')
# st.write('Your product is', product)

review = st.text_input('Your Review')
# st.write('Your Review is', review)

# tokenizer.fit_on_texts(review)
sequences = tokenizer.texts_to_sequences([review])


max_seq_length = max(len(seq) for seq in sequences)

padded_sequences = pad_sequences(sequences, maxlen=2699)

print(padded_sequences)
X = padded_sequences
prediction = model.predict(X)


st.write(f'Your rating Review Value According to Neural Network is: {prediction}')


