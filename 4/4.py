# Q4. Write a program to find the word Collocations. 

import nltk;
nltk.download('averaged_perceptron_tagger')
nltk.download('inaugural')
from nltk.corpus import inaugural, stopwords
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures


if __name__ == '__main__':
    words = [w.lower() for w in inaugural.words('1793-Washington.txt')]

    biagram_collocation = BigramCollocationFinder.from_words(words)
    
    stopset = set(stopwords.words('english'))
    filter_stops = lambda w: len(w) < 3 or w in stopset
    
    biagram_collocation.apply_word_filter(filter_stops)
    collocations = biagram_collocation.nbest(BigramAssocMeasures.likelihood_ratio, 15)
    print("Collocations in the given corpus are:")
    for pair in collocations:
        print(pair)
