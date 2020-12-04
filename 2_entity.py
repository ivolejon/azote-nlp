import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

def preprocess(sent):
    sent = nltk.word_tokenize(sent)
    sent = nltk.pos_tag(sent)
    return sent

text = "Cod fishing in the Baltic Sea is stopped in a new EU decision"

sent = preprocess(text)
print(sent)