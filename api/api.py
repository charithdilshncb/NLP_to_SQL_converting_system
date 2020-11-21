import flask
import nltk
from nltk.corpus import wordnet
from nltk.stem.wordnet import WordNetLemmatizer
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True
lemmatizer = WordNetLemmatizer()

@app.route('/', methods=['GET'])
def home():
    return '''<h2>NLP to SQL converting system</h2>'''

def get_wordnet_pos(word):
    """Map POS tag to first character lemmatize() accepts"""
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    return tag_dict.get(tag, wordnet.NOUN)

@app.route('/posTag',methods = ['GET'])
def postTag():
    sentence = request.args.get('sentense')

    # tokenize and lematize the sentence
    lemmatized_output = [lemmatizer.lemmatize(w, get_wordnet_pos(w)) for w in nltk.word_tokenize(sentence)]

    # POS Tag the sentence
    tagged = nltk.pos_tag(lemmatized_output)
    response = jsonify({"POS_Tags":tagged })
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

app.run()
