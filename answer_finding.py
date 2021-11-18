import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from tfidf_vectorizer_tracker import TfidfVectorizerTracker
from settings import ir_dataset, ir_tfidf_vectorizer_tracker


def retrieve_answer(question):
    question = pd.Series([question])

    answer, bad_match = get_likely_answer(question, ir_tfidf_vectorizer_tracker,
                                          dataset=ir_dataset)

    if len(answer) > 1:
        print("what did the didded that")
        answer, bad_match = get_likely_answer(question, TfidfVectorizerTracker(answer))

    return answer, bad_match


def get_likely_answer(information_request, tfidf_vectorizer_tracker, dataset=None):
    information_request_tf = tfidf_vectorizer_tracker.vectorizer.transform(information_request)
    tracker = tfidf_vectorizer_tracker.document_vector_tracker
    highest_score = 0
    bad_match = False
    top_result = ""

    for key in tracker:
        similarity_score = cosine_similarity(tracker[key], information_request_tf)[0][0]
        if similarity_score > highest_score:
            highest_score = similarity_score
            top_result = key

    if dataset is None:
        answer_list = [top_result]
    else:
        answer_list = list(dataset.loc[dataset['Question'] == top_result]['Answer'])

    if highest_score < 0.5:
        bad_match = True

    return answer_list, bad_match
