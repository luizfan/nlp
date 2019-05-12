# Analyze Text(PT-BR) with Python3 and NLTK


Code made for presentation of FCamara meetup

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install flask
```

```bash
pip install nltk
```

```bash
pip install pyyaml
```

```bash
pip install unicodedata
```


Open your python console and run it
```python
import nltk
nltk.download('rslp')
nltk.download('punkt')
```

## Run
Run server.py script
```python
py server.py
```

## Routes
Obs: 
The default port is 8081, but can be changed in code in server.py

```
GET /
Returns application status
```

Train the algorithm with phrases from code samples
```
GET /train
```


Train the algorithm with some sent phrase.
```
POST /train
body:
   phrase:'type something here'
   class: 'phrase class'
```

Returns class with higher matching and your score
```
GET /classify
body:
   phrase:'write something to be classified'

```

Talk to the robot
```
GET /chat
body:
   phrase:'write something'

```

teach the algorithm new answers
```
POST /answer
body:
   answer:'type something here'
   class: 'answer class'
```