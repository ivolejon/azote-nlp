import nltk
from nltk.stem import SnowballStemmer
 
stemmer = SnowballStemmer("swedish")
print (stemmer.stem("försöken"))
