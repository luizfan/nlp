import yaml
import nltk
import unicodedata
from nltk.stem import RSLPStemmer

def tokenize(sentence):
    sentence = sentence.lower()
    sentence = strip_accents(sentence)
    sentence = nltk.word_tokenize(sentence)
    return sentence

def stemming(sentence):
    stemmer = RSLPStemmer()
    phrase = []
    for word in sentence:
        phrase.append(stemmer.stem(word.lower()))
    return phrase

def remove_stopwords(sentence):
    stopwords = nltk.corpus.stopwords.words('portuguese')
    phrase = []
    for word in sentence:
        if word not in stopwords:
            phrase.append(word)
    return phrase

def strip_accents(sentence):
    try:
        sentence = unicode(sentence, 'utf-8')
    except NameError: # unicode is a default on python 3 
        pass

    sentence = unicodedata.normalize('NFD', sentence)\
           .encode('ascii', 'ignore')\
           .decode("utf-8")
    return str(sentence)


def save_corpus(w):
    fileW = open("corpus.nlp", 'w')
    fileW.write(str(w))
    fileW.close()

def load_corpus():
    fileW = open("corpus.nlp", 'r')
    words = fileW.read()
    fileW.close()
    words = yaml.load(words)
    if words is None:
        return {}
    return words
