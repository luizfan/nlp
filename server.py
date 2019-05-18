from flask import Flask,json,request
from train import learning,sample
from utils import save_corpus,normalize
from answer import return_answer,include_answer
from calculator import calculate_score

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def health_check():
    return create_response(200,{"status":"UP"})

@app.route("/train", methods = ['GET'])
def train_with_examples():
    save_corpus(learning(sample()))
    return create_response(200,{"status":"sample phrases included"})

@app.route("/train", methods = ['POST'])
def train():
    phrase = request.form.get('phrase')
    class_name = request.form.get('class')
    save_corpus(learning([{'class':class_name,'phrase':phrase}]))
    return create_response(200,{"status":"phrase included"})

@app.route("/classify", methods = ['GET'])
def classify():
    phrase = request.form.get('phrase')
    return create_response(200,calculate_score(phrase))

@app.route("/chat", methods = ['GET'])
def chat():
    phrase = request.form.get('phrase')
    return create_response(200,{'answer':return_answer(calculate_score(phrase)['classname'])})

@app.route("/answer", methods = ['POST'])
def save_answer():
    answer = request.form.get('answer')
    classname = request.form.get('class')
    include_answer(classname,answer)
    return create_response(200,{"status":"answer included"})

@app.route("/normalize", methods = ['GET'])
def return_normalize():
    phrase = request.form.get('phrase')
    return create_response(200,{"normalize":normalize(phrase)})

def create_response(statusCode, data):
    response = app.response_class(
        response=json.dumps(data),
        status=statusCode,
        mimetype='application/json'
    )
    return response

app.run(host='127.0.0.1', port=8081)