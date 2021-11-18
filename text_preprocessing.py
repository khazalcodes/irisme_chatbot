import re
import contractions
import nltk.downloader
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer

REMOVE_PUNCTUATION_REGEX = r"\b\w*[-']\w*\b|\w+[']|\w+"
wordnet_lemmatizer = WordNetLemmatizer()
posmap = {
    'ADJ': wordnet.ADJ,
    'ADV': wordnet.ADV,
    'NOUN': wordnet.NOUN,
    'VERB': wordnet.VERB
}


def clean_text(text: str) -> str:
    no_punctuation = re.findall(REMOVE_PUNCTUATION_REGEX, text)
    cleaned_text = " ".join(no_punctuation)
    return cleaned_text.lower()


def lemmatize_token(token: (str, str)) -> str:
    token_word = token[0]
    token_tag = token[1]
    if token_tag in posmap.keys():
        token_word = wordnet_lemmatizer.lemmatize(token_word, posmap[token_tag])
    return token_word


def preprocess_data(questions):
    # Filtering out all of the symbols and what not
    # Stop word filtration not used due to the limited number of words in each question
    for i in range(len(questions)):
        cleaned_text = contractions.fix(clean_text(questions[i]))
        parts_of_speech = nltk.pos_tag(word_tokenize(cleaned_text), tagset='universal')
        lemmatized_text = ' '.join(list(map(lemmatize_token, parts_of_speech)))
        questions[i] = lemmatized_text

    return questions


def preprocess_datum(question):
    # Filtering out all of the symbols and what not
    # Stop word filtration not used due to the limited number of words in each question
    cleaned_text = contractions.fix(clean_text(question))
    parts_of_speech = nltk.pos_tag(word_tokenize(cleaned_text), tagset='universal')
    lemmatized_text = ' '.join(list(map(lemmatize_token, parts_of_speech)))
    return lemmatized_text

