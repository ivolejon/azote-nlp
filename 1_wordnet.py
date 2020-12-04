from nltk.corpus import wordnet
text = "forest close"
words = text.split(" ")
# words = ["would","research","part","technologies","size","articles","analyzes","line"]
for w in words:
    syns = wordnet.synsets(w)
    if syns and syns[0].lexname().split('.')[0] == 'noun':
        if syns[0].lexname() not in ['noun.quantity']:
            # print(syns[0].lexname(), w)
            print(w, syns[0].lexname())
    # print(w, syns[0].lexname().split('.')[0]) if syns else (w, None)