from flask import Flask, request, jsonify
from flask_cors import CORS  #Import the CORS module for routes
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

app = Flask(__name__)
CORS(app)  #to enable CORS for all routes

# loading the tokenizer and model
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)
model = load_model('amazon_review.h5')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    product_review = data.get('productReview', '')

    sequences = tokenizer.texts_to_sequences([product_review])
    padded_sequences = pad_sequences(sequences, maxlen=2699)

    X = padded_sequences
    prediction = model.predict(X)

    return jsonify({'predicted_rating': float(prediction[0][0])})

if __name__ == '__main__':
    app.run(debug=True)






