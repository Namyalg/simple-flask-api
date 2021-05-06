import pickle

def classify_utterance(utt):
    # load the vectorizer
    loaded_vectorizer = pickle.load(open('/content/drive/MyDrive/PROJECT-FIR/vectorizer1.pickle', 'rb'))

    # load the model
    loaded_model = pickle.load(open('/content/drive/MyDrive/PROJECT-FIR/classification1.model', 'rb'))

    # make a prediction
    print(loaded_model.predict(loaded_vectorizer.transform([utt])))




text = "I was promised a job offer but was not given any offer and my details were stolen"
text1 = "I purchased a washing machine which costed 200 thousand ruppes but was given the fake product"

print(classify_utterance(text))
