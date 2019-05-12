import yaml
import nltk
import unicodedata
import codecs
from nltk.stem import RSLPStemmer

def tokenize(sentence):
    sentence = sentence.lower()
    sentence = strip_accents(sentence)
    sentence = nltk.word_tokenize(sentence)
    return sentence

def strip_accents(sentence):
    try:
        sentence = unicode(sentence, 'utf-8')
    except NameError: # unicode is a default on python 3 
        pass

    sentence = unicodedata.normalize('NFD', sentence)\
           .encode('ascii', 'ignore')\
           .decode("utf-8")
    return str(sentence)

def remove_stopwords(sentence):
    stopwords = load_stopword()
    phrase = []
    for word in sentence:
        if word not in stopwords:
            phrase.append(word)
    return phrase

def stemming(sentence):
    stemmer = RSLPStemmer()
    phrase = []
    for word in sentence:
        phrase.append(stemmer.stem(word.lower()))
    return phrase

def save_corpus(w):
    fileW = open("text/corpus.txt", 'w')
    fileW.write(str(w))
    fileW.close()

def load_corpus():
    with open("text/corpus.txt", "rb") as f:
        words = f.read().decode("UTF-8")
    words = yaml.load(words,Loader=yaml.FullLoader)
    if words is None:
        return {}
    return words

def load_stopword():
    with open('text/stopwords.txt', 'r') as f:
        stopwords = [strip_accents(line.strip()) for line in f] 
    return stopwords

def save_answer(w):
    fileW = codecs.open("text/answer.txt", "w", "utf-8")
    fileW.write(str(w))
    fileW.close()

def load_answer():
    with open("text/answer.txt", "rb") as f:
        answer = f.read().decode("UTF-8")
    answer = yaml.load(answer,Loader=yaml.FullLoader)
    if answer is None:
        return {}
    return answer
