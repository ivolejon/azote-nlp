# -*- coding: utf-8 -*-
import nltk
# from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

stemmer = SnowballStemmer("english")

# stopwords = stopwords.words('swedish')
stopwords = {'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now',}
input_text = "protect and restore - so we can save the coast's ecosystem human activities have for a long time reduced biodiversity and weakened the ecosystem's natural functions on the coast. in order to stop the loss of species and habitats and secure access to important ecosystem services, urgent efforts are needed, such as increased nature conservation and reduced strain from harmful activities. in some cases, active restoration is also required for coastal ecosystems to be able to recover. the swedish coasts are very popular areas for recreation and outdoor life. they offer invaluable opportunities for nature experiences and are the basis for a significant hospitality industry. the same coastal environments also contribute to the entire marine ecosystem by being homes and nurseries for many plant and animal species. but these social, economic and ecological values ​​are threatened by the influence of human activities. eutrophication, fishing, boat traffic, dredging and construction have a major impact on the coastal environment. the part of the coast that is in a natural state is continuously declining, as humans take up ever larger parts of nature. the loss of natural environments means that many species that are important for the ecosystem's function become less common and lead to lost nature and experience values. it also leads to a reduction in the ecosystem's production capacity and its resistance to additional loads. today, we are far from achieving the environmental goals for the coast that sweden has set nationally or together with other countries. this applies to the swedish environmental goals and objectives in the marine environment ordinance as well as those in the eu species and habitats directives and the global sustainability goals. ongoing climate change is putting additional pressure on coastal ecosystems and making it even more important to strengthen their natural resilience and resilience. research also shows that intact ecosystems can help mitigate the effects of climate change. in the coastal area, for example, seagrass beds act as carbon sinks, and vegetation in the beach area can stabilize the bottom and reduce the risk of erosion. these properties are also becoming increasingly important in line with climate change, which is leading to rising sea levels and stronger storms. coordinated action is needed to strengthen the conditions for species and their habitats, slow down the loss of biodiversity and achieve long-term sustainable use of the coast. we also need to act quickly."
words = input_text.split()
words_without_stopwords = [word for word in words if word not in stopwords]

for word in words_without_stopwords:
    word = lemmatizer.lemmatize(word, "v")
    print(word)
    

# final = " ".join(words_without_stopwords)

# print (final)