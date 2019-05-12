from utils import tokenize,stemming,remove_stopwords,load_corpus

def calculate_class_score(sentence,class_name):
    score = 0 
    sentence = tokenize(sentence)
    sentence = stemming(sentence)
    sentence = remove_stopwords(sentence)
    dados = load_corpus()
    for word in sentence:
        if word in dados[class_name]:
            score += dados[class_name][word]
    return score

def calculate_score(sentence):
    high_score = 0
    classname = 'default'
    dados = load_corpus()
    for classe in dados.keys():
        pontos = 0
        pontos = calculate_class_score(sentence,classe)
        if pontos > high_score:
            high_score = pontos
            classname = classe
    return {'classname':classname,'high_score':high_score}