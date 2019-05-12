from flask import Flask,json,request
from train import learning,train
from utils import save_corpus
from calculator import calculate_score

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def health_check():
    return create_response(200,{"status":"UP"})

@app.route("/training", methods = ['GET'])
def training():
    save_corpus(learning(train()))
    return create_response(200,{"status":"phrases included"})

@app.route("/classify", methods = ['GET'])
def classify():
    phrase = request.form.get('phrase')
    print(phrase)    
    return create_response(200,calculate_score(phrase))

def create_response(statusCode, data):
    response = app.response_class(
        response=json.dumps(data),
        status=statusCode,
        mimetype='application/json'
    )
    return response

app.run(host='127.0.0.1', port=8081)