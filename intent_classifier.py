import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score
from text_preprocessing import preprocess_data
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

# https://github.com/rahul051296/small-talk-rasa-stack/blob/master/data/nlu.md, I used this for my HI and ST part


class IntentClassifier:
    questions = []
    intents = []
    X_train = []
    X_test = []
    y_train = []
    y_test = []

    count_vectorizer = CountVectorizer()
    classifier = KNeighborsClassifier(n_neighbors=5)
    tfidf_transformer = TfidfTransformer(use_idf=True, sublinear_tf=True) # higher accuracy and f1 using this as aposed to TFIDFVECTORIZEErdf

    def __init__(self):
        self.inject_dataset()
        self.questions = preprocess_data(self.questions)
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.questions, self.intents,
                                                                                test_size=0.225, stratify=self.intents,
                                                                                random_state=1,)
        X_train_counts = self.count_vectorizer.fit_transform(self.X_train)
        X_train_tf = self.tfidf_transformer.fit_transform(X_train_counts)
        self.classifier.fit(X_train_tf, self.y_train)

    def inject_dataset(self):
        dataset = pd.read_csv("IntentClassifierDataset.csv")
        for _, row in dataset.iterrows():
            self.questions.append(row['Question'])
            self.intents.append(row['Intent'])

    def predict_intent(self, new_intent):
        processed_new_data = self.tfidf_transformer.transform(self.count_vectorizer.transform([new_intent]))
        prediction = self.classifier.predict(processed_new_data)
        return "".join(prediction)
