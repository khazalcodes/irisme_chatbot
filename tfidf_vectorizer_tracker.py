from sklearn.feature_extraction.text import TfidfVectorizer
from text_preprocessing import preprocess_data, preprocess_datum


class TfidfVectorizerTracker:
    vectorizer = None
    pre_post_pairs = None
    vector_space = None  # Where we store the vectorizer.fit_transform
    document_vector_tracker = None  # Where we pair up each document (question) to its tfidf value

    def __init__(self, documents):
        self.vectorizer = TfidfVectorizer(use_idf=True, sublinear_tf=True)
        self.pre_post_pairs = {}
        for document in documents:
            self.pre_post_pairs[document] = preprocess_datum(document)
        preprocessed_documents = preprocess_data(documents)
        self.vector_space = self.vectorizer.fit_transform(preprocessed_documents)
        self.document_vector_tracker = {}
        for document, preprocessed_document in self.pre_post_pairs.items():
            self.document_vector_tracker[document] = self.vectorizer.transform([preprocessed_document])
