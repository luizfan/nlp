from utils import tokenize,stemming,remove_stopwords

def learning(training_data):
    corpus_words = {}
    for data in training_data:
        phrase = data['phrase']
        phrase = tokenize(phrase)
        phrase = stemming(phrase)
        phrase = remove_stopwords(phrase)
        class_name = data['class']
        if class_name not in list(corpus_words.keys()):
            corpus_words[class_name] = {}
        for word in phrase:
            if word not in list(corpus_words[class_name].keys()):
                corpus_words[class_name][word] = 1
            else:
                corpus_words[class_name][word] += 1
    return corpus_words


def train():
    training_data = []
    training_data.append({"class":"amor", "phrase":"Eu te amo"})
    training_data.append({"class":"amor", "phrase":"Você é o amor da minha vida"})
    training_data.append({"class":"medo", "phrase":"estou com medo"})
    training_data.append({"class":"medo", "phrase":"tenho medo de fantasma"})
    print("%s phrases included" % len(training_data))
    return training_data