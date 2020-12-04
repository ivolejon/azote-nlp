import os
from flask import Flask,request, jsonify, render_template
from summa import summarizer
from nlp_rake import Rake
from summa import keywords



rake = Rake( max_words=2, min_chars=3, min_freq=1)

template_dir = os.path.abspath('.')
app = Flask(__name__,template_folder=template_dir)
@app.route('/')
def hello_world():
    return render_template("index.html")

def geteKeywords(input_text):
    return keywords.keywords(input_text, split=True)

def getKeyPhrases(input_text):
    return summarize(input_text)


def summarize(input_text):
    text = summarizer.summarize(input_text)
    if not text:
        return getPhrases(input_text)
    else:
        return getPhrases(input_text)

def getPhrases(input_text):
    return rake.apply(input_text)

@app.route('/keywords', methods = ['POST'])
def phrase():
    phrases = []
    input_text = request.form['input_text'] or ""

    key_phrases = summarize(input_text)
    for tup in key_phrases:
        if tup[1] <= 1:
            del tup
        else:
            phrases.append({"text":tup[0], "score":tup[1]})

    keywords = geteKeywords(input_text)
    for w in keywords:
        phrases.append({"text":w, "score":10})
    
    phrases = sorted(phrases, key = lambda i: i['score'],reverse=True)

    return jsonify(phrases)


if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)